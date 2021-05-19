# all the function of django project are here!!

from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
from django.core.files.storage import FileSystemStorage



def button(request):  # render the home page
    return render(request, 'home.html')

def abc(request):  # render the home page
    return render(request, 'abc.html')

def home(request):  # render the home page
    return render(request, 'home.html')

def us(request):  # render the home page
    return render(request, 'us.html')


def b64d(request):
    inp = request.POST.get('b')
    out = run([sys.executable, 'E://Submission//Minor_Project-1//tools//base64d.py', inp],
              shell=False, stdout=PIPE)
    print(out)

    return render(request, 'abc.html', {'b64d': out.stdout.decode('UTF-8')})

def b64e(request):
    inp = request.POST.get('c')
    out = run([sys.executable, 'E://Submission//Minor_Project-1//tools//base64e.py', inp],
              shell=False, stdout=PIPE)
    print(out)

    return render(request, 'abc.html', {'b64e': out.stdout.decode('UTF-8')})

def b32d(request):
    inp = request.POST.get('b32d')
    out = run([sys.executable, 'E://Submission//Minor_Project-1//tools//base32d.py', inp],
              shell=False, stdout=PIPE)
    print(out)

    return render(request, 'abc.html', {'b32d': out.stdout.decode('UTF-8')})

def b32e(request):
    inp = request.POST.get('b32e')
    out = run([sys.executable, 'E://Submission//Minor_Project-1//tools//base32e.py', inp],
              shell=False, stdout=PIPE)
    print(out)

    return render(request, 'abc.html', {'b32e': out.stdout.decode('UTF-8')})

def b86d(request):
    inp = request.POST.get('b86d')
    out = run([sys.executable, 'E://Submission//Minor_Project-1//tools//base86d.py', inp],
              shell=False, stdout=PIPE)
    print(out)

    return render(request, 'abc.html', {'b86d': out.stdout.decode('UTF-8')})

def b86e(request):
    inp = request.POST.get('b86e')
    out = run([sys.executable, 'E://Submission//Minor_Project-1//tools//base86e.py', inp],
              shell=False, stdout=PIPE)
    print(out)

    return render(request, 'abc.html', {'b86e': out.stdout.decode('UTF-8')})

def sherlock(request):
    inp = request.POST.get('s')
    out = run([sys.executable, 'E://Submission//Minor_Project-1//tools//sherlock//sherlock//sherlock.py', inp],
              shell=False, stdout=PIPE)
    print(out)
    return render(request, 'abc.html', {'sher': out.stdout.decode('UTF-8')})

def rotd(request):
    inp = request.POST.get('rotd')
    inp1 = request.POST.get('keyd')
    out = run([sys.executable, 'E://Submission//Minor_Project-1//tools//ROTd.py', inp, inp1],
              shell=False, stdout=PIPE)
    print(out)
    return render(request, 'abc.html', {'rotd': out.stdout.decode('UTF-8')})

def rote(request):
    inp = request.POST.get('rote')
    inp1 = request.POST.get('keye')
    out = run([sys.executable, 'E://Submission//Minor_Project-1//tools//ROTe.py', inp, inp1],
              shell=False, stdout=PIPE)
    print(out)
    return render(request, 'abc.html', {'rote': out.stdout.decode('UTF-8')})

def caeserd(request):
    inp = request.POST.get('caesard')
    inp1 = request.POST.get('keyd')
    out = run([sys.executable, 'E://Submission//Minor_Project-1//tools//caesard.py', inp, inp1],
              shell=False, stdout=PIPE)
    print(out)
    return render(request, 'abc.html', {'caesard': out.stdout.decode('UTF-8')})

def caesere(request):
    inp = request.POST.get('caesare')
    inp1 = request.POST.get('keye')
    out = run([sys.executable, 'E://Submission//Minor_Project-1//tools//caesare.py', inp, inp1],
              shell=False, stdout=PIPE)
    print(out)
    return render(request, 'abc.html', {'caesare': out.stdout.decode('UTF-8')})

def morsed(request):
    inp = request.POST.get('morsed')
    out = run([sys.executable, 'E://Submission//Minor_Project-1//tools//MORSEd.py', inp],
              shell=False, stdout=PIPE)
    print(out)
    return render(request, 'abc.html', {'morsed': out.stdout.decode('UTF-8')})

def morsee(request):
    inp = request.POST.get('morsee')
    out = run([sys.executable, 'E://Submission//Minor_Project-1//tools//MORSEe.py', inp],
              shell=False, stdout=PIPE)
    print(out)
    return render(request, 'abc.html', {'morsee': out.stdout.decode('UTF-8')})

def bacond(request):
    inp = request.POST.get('bacond')
    out = run([sys.executable, 'E://Submission//Minor_Project-1//tools//BACONd.py', inp],
              shell=False, stdout=PIPE)
    print(out)
    return render(request, 'abc.html', {'bacond': out.stdout.decode('UTF-8')})

def bacone(request):
    inp = request.POST.get('bacone')
    out = run([sys.executable, 'E://Submission//Minor_Project-1//tools//BACONe.py', inp],
              shell=False, stdout=PIPE)
    print(out)
    return render(request, 'abc.html', {'bacone': out.stdout.decode('UTF-8')})

def vigenered(request):
    inp = request.POST.get('vigenered')
    inp1 = request.POST.get('keyd')
    out = run([sys.executable, 'E://Submission//Minor_Project-1//tools//VIGENEREd.py', inp, inp1],
              shell=False, stdout=PIPE)
    print(out)
    return render(request, 'abc.html', {'vigenered': out.stdout.decode('UTF-8')})

def vigeneree(request):
    inp = request.POST.get('vigeneree')
    inp1 = request.POST.get('keye')
    out = run([sys.executable, 'E://Submission//Minor_Project-1//tools//VIGENEREe.py', inp, inp1],
              shell=False, stdout=PIPE)
    print(out)
    return render(request, 'abc.html', {'vigeneree': out.stdout.decode('UTF-8')})
