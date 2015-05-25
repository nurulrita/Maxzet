from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View, DetailView
from .models import *
from .forms import *

class HomeView(View):
    template_name = 'maxzet/home.html'

    def get(self,request):
        

        return render(request,self.template_name)

class TransaksiWomenView(View):
	id=None
	template_name = 'maxzet/barang/transaksi-women.html'
	def get(self,request,id=None):
		ID=Women.objects.get(pk=id)
		pembeli=UserProfile.objects.get(user=request.user)
		form=TransaksiFormWomen(initial={'pilihan_alamat':'P','alamat_pengiriman':pembeli.alamat})

		return render(request,self.template_name,{'form':form,'id':ID})
	def post(self,request,id=None):
		form=TransaksiFormWomen(request.POST or None)
		
		ID=Women.objects.get(pk=id)
		if form.is_valid():
			transaksi=form.save(commit=False)
			transaksi.barang=ID
			transaksi.pembeli=request.user
			almt=form.cleaned_data['alamat_pengiriman']
			if almt:
				transaksi.alamat_pengiriman=almt
			else:
				transaksi.alamat_pengiriman=request.user.alamat

			transaksi.total_bayar=int(form.cleaned_data['banyaknya'])*ID.harga
			transaksi.save()
			
		#return HttpResponseRedirect(reverse('women'))
		messages.success(request,'Pemesanan Berhasil')
		return HttpResponseRedirect(reverse('women'))

class TransaksiMenView(View):
	id=None
	template_name = 'maxzet/barang/transaksi-men.html'
	def get(self,request,id=None):
		ID=Men.objects.get(pk=id)
		pembeli=UserProfile.objects.get(user=request.user)
		form=TransaksiFormMen(initial={'pilihan_alamat':'P','alamat_pengiriman':pembeli.alamat})

		return render(request,self.template_name,{'form':form,'id':ID})
	def post(self,request,id=None):
		form=TransaksiFormMen(request.POST or None)
		
		ID=Men.objects.get(pk=id)
		if form.is_valid():
			transaksi=form.save(commit=False)
			transaksi.barang=ID
			transaksi.pembeli=request.user
			almt=form.cleaned_data['alamat_pengiriman']
			if almt:
				transaksi.alamat_pengiriman=almt
			else:
				transaksi.alamat_pengiriman=request.user.alamat

			transaksi.total_bayar=int(form.cleaned_data['banyaknya'])*ID.harga
			transaksi.save()
			
		#return HttpResponseRedirect(reverse('men'))
		messages.success(request,'Pemesanan Berhasil')
		return HttpResponseRedirect(reverse('men'))


class BarangMenDetailView(DetailView):
	model = Men
	template_name = 'maxzet/barang/detail-barang-men.html'

class BarangWomenDetailView(DetailView):
	model = Women
	template_name = 'maxzet/barang/detail-barang-women.html'

class MenView(View):
    template_name = 'maxzet/barang/all-barang-men.html'

    def get(self,request):
        barang = Men.objects.all()

        return render(request,self.template_name,{'barang':barang})

class MenCategoryView(View):
    template_name = 'maxzet/barang/all-barang-men.html'

    def get(self,request,category):
        barang = Men.objects.filter(category)

        return render(request,self.template_name,{'barang':barang})

class WomenView(View):
    template_name = 'maxzet/barang/all-barang-women.html'

    def get(self,request):
        barang = Women.objects.all()
	
        return render(request,self.template_name,{'barang':barang})

class About(View):
    template_name = 'maxzet/about.html'

    def get(self,request):
        

        return render(request,self.template_name)

class Help(View):
    template_name = 'maxzet/help.html'

    def get(self,request):
        

        return render(request,self.template_name)
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                #redirect to disable account msg
                messages.error(request,'Not cool enough')
                return HttpResponseRedirect(reverse('login'))
        else:
            #invalid login
            messages.error(request,'Incorrect Username/Password')
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'maxzet/user/login.html')
    
def register(request):
   
    registered = False
   
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            
            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()


    return render(request,
            'maxzet/user/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )
