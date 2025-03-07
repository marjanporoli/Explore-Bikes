import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from app1.models import *


# Create your views here.
# Public Home - Index html part
def index(request):
    return render(request, "public/index.html", {"title": "Explore Bikes"})


def view_services_public(request):
    data = tbl_service.objects.all()
    return render(request, "public/view_services_public.html", {"title": "View Service", "datas": data})


def view_reviews_public(request):
    data = tbl_reviews.objects.all()
    return render(request, "public/view_reviews_public.html", {"title": "View Review", "datas": data})


def view_vehicles_public(request):
    data = tbl_vehicle_model.objects.all()
    return render(request, "public/view_vehicles_public.html", {"title": "View Vehicles", "datas": data})


# Headers

# Admin Header
def admin(request):
    return render(request, "header/admin.html", {"title": "Admin"})


# Sales Header
def sales(request):
    return render(request, "header/sales.html", {"title": "Sales"})


# Service Header
def service(request):
    return render(request, "header/service.html", {"title": "Service"})


# Customer Header
def customer(request):
    return render(request, "header/customer.html", {"title": "Customer"})


# Public Header
def public(request):
    return render(request, "header/public.html", {"title": "Public"})


################################################# Home #################################################

def admin_home(request):
    return render(request, 'home/admin.html', {"title": "Admin Home"})


def customer_home(request):
    return render(request, 'home/customer.html', {"title": "Customer Home"})


def sales_home(request):
    return render(request, 'home/sales.html', {"title": "Sales Home"})


def service_home(request):
    return render(request, 'home/service.html', {"title": "Service Home"})


# Forms

# Admin -> Staff Management -> Appointment
def appointment(request):
    return render(request, "forms/appointment.html", {"title": "Staff Appointment"})


def appoint(request):
    if request.method == "POST":
        data = tbl_staff()
        data.staffID = "na"
        data.Name = request.POST.get('name')
        data.Address = request.POST.get('address')
        data.Phone = request.POST.get('phone')
        data.Email = request.POST.get('email')
        data.category = request.POST.get('category')
        data.save()
        data.staffID = "EBS" + data.category + str(data.id)
        data.save()
        data1 = tbl_login()
        data1.userid = data.staffID
        data1.password = request.POST.get('phone')
        data1.category = request.POST.get('category')
        data1.save()
        return render(request, "forms/appointment.html", {"title": "Staff Appointment"})


# Admin -> Vehicle Master -> New Model
def new_model(request):
    return render(request, "forms/new_model.html", {"title": "New Model"})


def add_new_model(request):
    if request.method == "POST":
        data = tbl_vehicle_model()
        data.vehiclemodelnumber = request.POST.get('modelnumber')
        data.name = request.POST.get('name')
        data.enginecapacity = request.POST.get('enginecapacity')
        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo)
        uploaded_file_url = fs.url(filename)
        data.photo = uploaded_file_url
        data.cc = request.POST.get('cc')
        data.tankcapacity = request.POST.get('tankcapacity')
        data.mileage = request.POST.get('mileage')
        data.colour = request.POST.get('colour')
        data.price = request.POST.get('price')
        data.save()
        return render(request, "forms/new_model.html", {"title": "New Model"})


# Admin -> Spare Parts -> Add Parts
def add_part(request):
    return render(request, "forms/add_part.html", {"title": "Add Part"})


def add_new_part(request):
    if request.method == "POST":
        data = tbl_spare_parts()
        data.sparepartnumber = request.POST.get('sparepartnumber')
        data.name = request.POST.get('name')
        data.description = request.POST.get('description')
        data.photo = request.POST.get('photo')
        data.unit = request.POST.get('unit')
        data.price = request.POST.get('price')
        data.stockquantity = request.POST.get('stockquantity')
        data.save()
    return render(request, "forms/add_part.html", {"title": "Add Part"})


# Admin -> Service Master -> New Service
def new_service(request):
    return render(request, "forms/new_service.html", {"title": "New Service"})


def add_new_service(request):
    if request.method == "POST":
        data = tbl_service()
        data.serviceID = "na"
        data.servicename = request.POST.get('servicename')
        data.save()
        data.serviceID = "SRV" + str(data.id)
        data.save()
    return render(request, "forms/new_service.html", {"title": "New Service"})


# Customer -> Give Review
def give_review(request):
    return render(request, "forms/give_review.html", {"title": "Give Review"})


def new_give_review(request):
    if request.method == "POST":
        data = tbl_reviews()
        data.reviewID = "na"
        data.customerID = "na"
        data.review = request.POST.get('review')
        data.reviewdate = datetime.datetime.now().strftime("%Y-%m-%d")
        data.save()
        data.customerID = request.session['uid']
        data.reviewID = "EBReview" + str(data.id)
        return render(request, "forms/give_review.html", {"title": "Give Review"})


# Customer -> Give Complaint
def give_complaint(request):
    return render(request, "forms/give_complaint.html", {"title": "Give Complaint"})


def new_give_complaint(request):
    if request.method == "POST":
        data = tbl_complaints()
        data.complaintID = "na"
        data.customerID = request.session['uid']
        data.complaint = request.POST.get('complaint')
        data.complaintDate = datetime.datetime.now().strftime("%Y-%m-%d")
        data.save()
        data.complaintID = "EBComplaint" + str(data.id)
        data.save()
        return render(request, "forms/give_complaint.html", {"title": "Give Complaint"})


# Public -> Register
def register(request):
    return render(request, "forms/register.html", {"title": "Register"})


def new_register(request):
    if request.method == "POST":
        data = tbl_customer()
        data.Customerid = "na"
        data.Name = request.POST.get('name')
        data.Address = request.POST.get('address')
        data.Phone = request.POST.get('phone')
        data.Email = request.POST.get('email')
        data.Password = request.POST.get('password')
        data.save()
        data.Customerid = "EBC" + str(data.id)
        data.save()
        data1 = tbl_login()
        data1.userid = "EBC" + str(data.id)
        data1.password = request.POST.get('password')
        data1.category = "Customer"
        data1.save()
    return render(request, "forms/register.html", {"title": "Register"})


##############

def remove_service(request):
    data = tbl_service.objects.all()
    return render(request, "tables/remove_service.html", {"title": "Service Display", "services": data})


def remove_service_functions(request, id):
    data = tbl_service.objects.get(id=id)
    data.delete()
    return redirect('/remove_service')


def update_service(request, id):
    data = tbl_service.objects.get(id=id)
    return render(request, "forms/update_service.html", {'title': 'Update Service', 'data': data})


def change_service(request, id):
    data = tbl_service.objects.get(id=id)
    data.servicename = request.POST.get('servicename')
    data.save()
    return redirect('/remove_service')


def book_service(request):
    data = tbl_service.objects.all().order_by('servicename')
    return render(request, 'booking/book_service.html', {"title": "book_service", "data": data})


def book_service_now(request, id):
    data = tbl_book_service()
    sdata = tbl_service.objects.get(id=id)
    data.serviceID = sdata.id
    data.customerID = request.session['uid']
    data.serviceName = sdata.servicename
    data.serviceID = "na"
    data.status = "pending"
    data.serviceDate = datetime.datetime.now().strftime("%Y-%m-%d")
    data.save()
    data.serviceID = "EBService" + str(data.id)
    return redirect('/book_service')


##############


def remove_staff(request):
    data = tbl_staff.objects.all()
    return render(request, "tables/remove_staff.html", {'staffs': data, 'title': 'Staff Display'})


def remove_staff_functions(request, id):
    data = tbl_staff.objects.get(id=id)
    data.delete()
    return redirect('/remove_staff')


def update_staff(request, id):
    data = tbl_staff.objects.get(id=id)
    return render(request, "forms/update_staff.html", {'title': 'Update Service', 'data': data})


def change_staff(request, id):
    data = tbl_staff.objects.get(id=id)
    data.Name = request.POST.get('name')
    data.Address = request.POST.get('address')
    data.Phone = request.POST.get('phone')
    data.Email = request.POST.get('email')
    data.save()
    return redirect('/remove_staff')


##############


def remove_price(request):
    data = tbl_spare_parts.objects.all()
    return render(request, "tables/remove_spare.html", {'parts': data, 'title': 'Staff Display'})


def remove_price_functions(request, id):
    data = tbl_spare_parts.objects.get(id=id)
    data.delete()
    return redirect('/remove_price')


def update_spare(request, id):
    data = tbl_spare_parts.objects.get(id=id)
    return render(request, "forms/update_spare.html", {'title': 'Update Spare', 'data': data})


def change_spare(request, id):
    data = tbl_spare_parts.objects.get(id=id)
    data.sparepartnumber = request.POST.get('sparepartnumber')
    data.name = request.POST.get('name')
    data.description = request.POST.get('description')
    data.photo = request.POST.get('photo')
    data.unit = request.POST.get('unit')
    data.price = request.POST.get('price')
    data.stockquantity = request.POST.get('stockquantity')
    data.save()
    return redirect('/remove_price')


##############


def remove_vehicle(request):
    data = tbl_vehicle_model.objects.all()
    return render(request, "tables/remove_vehicle.html", {'vehicles': data, 'title': 'Staff Display'})


def remove_vehicle_functions(request, id):
    data = tbl_vehicle_model.objects.get(id=id)
    data.delete()
    return redirect('/remove_vehicle')


def update_vehicle(request, id):
    data = tbl_vehicle_model.objects.get(id=id)
    return render(request, "forms/update_vehicle.html", {'title': 'Update Vehicle', 'data': data})


def change_vehicle(request, id):
    data = tbl_vehicle_model.objects.get(id=id)
    data.vehiclemodelnumber = request.POST.get('modelnumber')
    data.name = request.POST.get('name')
    data.enginecapacity = request.POST.get('enginecapacity')
    data.photo = request.POST.get('photo')
    data.cc = request.POST.get('cc')
    data.tankcapacity = request.POST.get('tankcapacity')
    data.mileage = request.POST.get('mileage')
    data.colour = request.POST.get('colour')
    data.price = request.POST.get('price')
    data.save()
    return redirect('/remove_vehicle')


def book_vehicle(request, id):
    data = tbl_vehicle_model.objects.get(id=id)
    return render(request, 'booking/book_vehicle.html', {"title": "book_vehicle", "data": data})


def book_vehicle_now(request, id):
    veh_data = tbl_vehicle_model.objects.get(id=id)
    data = tbl_booking()
    data.vehicle_model_number = veh_data.name
    data.customer_id = request.session['uid']
    data.booking_id = "na"
    data.booking_date = datetime.datetime.now().strftime("%Y-%m-%d")
    data.status = "pending"
    data.save()
    data.booking_id = "booking" + str(data.id)
    data.save()
    return redirect('/customer_home')


# Login page
def login(request):
    return render(request, 'forms/login.html')


def log(request):
    if request.method == 'POST':
        dataa = tbl_login.objects.all()
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        flag = 0
        for da in dataa:
            if un == da.userid and pwd == da.password:
                type = da.category
                request.session['uid'] = un
                flag = 1
                if type == "admin":
                    return redirect('/admin_home')
                elif type == "Customer":
                    return redirect('/customer_home')
                elif type == "Sales":
                    return redirect('/sales_home')
                elif type == "Service":
                    return redirect('/service_home')
                else:
                    return HttpResponse("Invalid acct type")
        if flag == 0:
            return HttpResponse("Invalid user")


###########
# Customer -> View Model
def view_model_page(request):
    data = tbl_vehicle_model.objects.all()
    return render(request, 'customer/view_model.html', {"title": "view_model_page", "models": data})


def customer_logout(request):
    return redirect("/login")


def view_booking_sales(request):
    data = tbl_booking.objects.all().filter(status="pending")
    return render(request, "sales/view_booking_sales.html", {"data": data})


def vehicle_booking_accept(request, id):
    data = tbl_booking.objects.get(id=id)
    data.status = "accepted"
    data.save()
    data_sales = tbl_sales()
    data_sales.vehicle_number = data.vehicle_model_number
    data_sales.customerID = data.customer_id
    data_sales.sales_no = "EBSalesNo" + str(data_sales.id)
    data_sales.save()
    return redirect('/view_booking_sales')


def vehicle_booking_reject(request, id):
    data = tbl_booking.objects.get(id=id)
    data.status = "rejected"
    data.save()
    return redirect('/view_booking_sales')


def view_booking_service(request):
    data = tbl_book_service.objects.all().filter(status="pending")
    return render(request, "service/view_booking_service.html", {"data": data})


def service_accept(request, id):
    data = tbl_book_service.objects.get(id=id)
    data.status = "accepted"
    data.save()
    return redirect('/view_booking_service')


def service_reject(request, id):
    data = tbl_book_service.objects.get(id=id)
    data.status = "rejected"
    data.save()
    return redirect('/view_booking_service')
