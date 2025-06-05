from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('HAAAAAAAAALOOOOOOOOO')

def about(request):
    return HttpResponse('HALAMAN PERTAMA')

def rumah(request):
    judul = 'rumah'
    isi = 'Bagian Isi'
    data = {
        'title' : judul,    
        'isi' : isi
    }
        
    
    return render(request, 'index.html')

def tentang(request):
    return render(request, 'profil/index.html')