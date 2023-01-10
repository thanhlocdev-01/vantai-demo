from django.shortcuts import render, redirect

from django.apps import apps 
import pymysql  
from .forms import CarForm, VexeForm
# Create your views here.

def connection():
    s = '127.0.0.1' 
    d = 'db_vantai' 
    u = 'root' 
    p = '' 
    conn = pymysql.connect(host=s, user=u, password=p, database=d)
    return conn

def carslist(request):
    cars = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TblKhachHang")
    for row in cursor.fetchall():
        cars.append({"id": row[0], "name": row[1], "phone": row[2], "email": row[3], "address": row[4], "diemdi": row[5], "diemden": row[6], "date": row[7]})
    conn.close()
    return render(request, 'vantai_views/carslist.html', {'cars':cars})

def addcar(request):
    if request.method == 'GET':
        return render(request, 'vantai_views/addcar.html')
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get("id")
            name = form.cleaned_data.get("name")
            phone = form.cleaned_data.get("phone")
            email = form.cleaned_data.get("email")
            address = form.cleaned_data.get("address")
            diemdi = form.cleaned_data.get("diemdi")
            diemden = form.cleaned_data.get("diemden")
            date = form.cleaned_data.get("date")
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TblKhachHang (id, name, phone, email, address, diemdi, diemden, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (id, name, phone, email, address, diemdi, diemden, date))
        conn.commit()
        conn.close()
        #return redirect('carslist')# chưa updatecar
        return render(request, 'vantai_views/addcar.html', {'car':{}})# ĐÃ updatecar


def updatecar(request, id):
    cr = []
    conn = connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM TblKhachHang WHERE id = %s", (id))
        for row in cursor.fetchall():
            cr.append({"id": row[0], "name": row[1], "phone": row[2], "email": row[3], "address": row[4], "diemdi": row[5], "diemden": row[6], "date": row[7]})
        conn.close()
        return render(request, 'vantai_views/addcar.html', {'car':cr[0]})
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            name = str(form.cleaned_data.get("name"))
            phone = int(form.cleaned_data.get("phone"))
            email = str(form.cleaned_data.get("email"))
            address = str(form.cleaned_data.get("address"))
            diemdi = str(form.cleaned_data.get("diemdi"))
            diemden = str(form.cleaned_data.get("diemden"))
            date = str(form.cleaned_data.get("date"))
            cursor.execute("UPDATE TblKhachHang SET name = %s, phone = %s, email = %s, address = %s, diemdi = %s, diemden = %s, date = %s WHERE id = %s", (name, phone, email, address, diemdi, diemden, date, id))
            conn.commit()
        conn.close()
        return redirect('carslist')
    
    
def deletecar(request, id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TblKhachHang WHERE id = %s", (id))
    conn.commit()
    conn.close()
    return redirect('carslist')

#Các trang chính
def myIndex(request):
    return  render(request, 'vantai_views/index.html')

def lichTrinh(request):
    return render(request,  'vantai_views/lichTrinh.html')

def login(request):
    return render(request, 'vantai_views/login.html')

def chart(request):
    return render(request, 'vantai_views/chart.html')

def dashboard(request):
    return render(request, 'vantai_views/indexdb.html')


def carsvexe(request):
    cars = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TblTuyenXe")
    for row in cursor.fetchall():
        cars.append({"id": row[0], "diemdi": row[1], "diemden": row[2], "date": row[3], "giave": row[4]})
    conn.close()
    return render(request, 'vantai_views/carsvexe.html', {'cars':cars})

def addvexe(request):
    if request.method == 'GET':
        return render(request, 'vantai_views/addvexe.html')
    if request.method == 'POST':
        form = VexeForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get("id")
            diemdi = form.cleaned_data.get("diemdi")
            diemden = form.cleaned_data.get("diemden")
            date = form.cleaned_data.get("date")
            giave = form.cleaned_data.get("giave")
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TblTuyenXe (id, diemdi, diemden, date, giave) VALUES (%s, %s, %s, %s, %s)", (id, diemdi, diemden, date, giave))
        conn.commit()
        conn.close()
        #return redirect('carslist')# chưa updatecar
        return render(request, 'vantai_views/addvexe.html', {'car':{}})
    
def updatevexe(request, id):
    cr = []
    conn = connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM TblTuyenXe WHERE id = %s", (id))
        for row in cursor.fetchall():
            cr.append({"id": row[0], "diemdi": row[1], "diemden": row[2], "date": row[3], "giave": row[4]})
        conn.close()
        return render(request, 'vantai_views/addvexe.html', {'car':cr[0]})
    if request.method == 'POST':
        form = VexeForm(request.POST)
        if form.is_valid():
            diemdi = form.cleaned_data.get("diemdi")
            diemden = form.cleaned_data.get("diemden")
            date = form.cleaned_data.get("date")
            giave = form.cleaned_data.get("giave")
            cursor.execute("UPDATE TblTuyenXe SET diemdi = %s, diemden = %s, date = %s, giave = %s WHERE id = %s", (diemdi, diemden, date, giave, id))
            conn.commit()
        conn.close()