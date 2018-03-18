#coding:utf-8
from django.shortcuts import render
from django.http import *
#from django.template import RequestContext,loader
from .models import *

# Create your views here.

def index(request):
#	temp = loader.get_template('booktest/index.html')
#	return HttpResponse(temp.render())
	booklist = BookInfo.objects.all()
	context = {'list':booklist}
	return render(request,'booktest/index.html',context)

def vmx(request):
        import libvirt
        conn = libvirt.open("qemu+tcp://192.168.137.131/system")
        #获取运行和挂起虚拟机的主机名列表
        run_list=[]
        suspend_list=[]
        for id in conn.listDomainsID():
            myDom = conn.lookupByID(id)
            if myDom.state()[0]==1:
                run_list.append(myDom.name())
            elif myDom.state()[0]==3:
                suspend_list.append(myDom.name())
            else:
                print 'error' 

        #获取未运行虚拟机的主机名列表
        shut_list=conn.listDefinedDomains()
            
        #构造上下文
        context={'run_list':run_list,'shut_list':shut_list,'suspend_list':suspend_list}

        return render(request,'booktest/vmx_index.html',context)

def start(request,name):
        import libvirt
        conn = libvirt.open("qemu+tcp://192.168.137.131/system")
        myDom = conn.lookupByName(name)
        myDom.create()
        while True:
            if myDom.state()[0]==1:
                break
        conn.close()    
        return HttpResponseRedirect('/vmx')

def stop(request,name):
        import libvirt
        conn = libvirt.open("qemu+tcp://192.168.137.131/system")
        myDom = conn.lookupByName(name)
        myDom.shutdown()
        while True:
            if myDom.state()[0]==5:
                break
        conn.close()    
        return HttpResponseRedirect('/vmx')

def suspend(request,name):
        import libvirt
        conn = libvirt.open("qemu+tcp://192.168.137.131/system")
        myDom = conn.lookupByName(name)
        myDom.suspend()
        while True:
            if myDom.state()[0]==3:
                break
        conn.close()    
        return HttpResponseRedirect('/vmx')

def resume(request,name):
        import libvirt
        conn = libvirt.open("qemu+tcp://192.168.137.131/system")
        myDom = conn.lookupByName(name)
        myDom.resume()
        while True:
            if myDom.state()[0]==1:
                break
        conn.close()    
        return HttpResponseRedirect('/vmx')

def show(request,id):
	book = BookInfo.objects.get(pk=id)
	herolist = book.heroinfo_set.all()
	context = {'list':herolist}

	return render(request,'booktest/show.html',context)
