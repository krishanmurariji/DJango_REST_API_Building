from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Group , Product,Storage,Name,Todo,Contacts

def base(request):
    return render(request,'base.html')

def home(request):
    data = Storage.objects.all().values()
    data2 = Contacts.objects.all().values()
    context = {'data':data, 'data2':data2 }
    return render(request,'home.html',context)

# Create your views here.

def contact(request):
    data = Name.objects.all().values()
    showinfo = {"data":data}
    return render(request,'contact.html',showinfo)

def form(request):
    data = Product.objects.all().values()
    context = {'data':data}
    return render(request,'form.html',context)

def savedata(request):
    name = request.POST.get('name')
    id = request.POST.get('id')
    price = request.POST.get('price')
    data = Product(pid = id, pname = name, pprice = price)
    data.save()
    return redirect('form')


def savename(request):
    firstname = request.POST.get('fn')
    lastname = request.POST.get('ln')
    data = Name(fname = firstname, lname = lastname)
    data.save()
    return redirect('contact')

def delname(request):
    if request.method == "POST":
        dfname = request.POST.get('fn')
        dlname = request.POST.get('ln')

        try:
            name_objs = Name.objects.filter(fname=dfname, lname=dlname)
            if name_objs:
                name_objs.delete()
                message = "Name(s) deleted successfully"
            else:
                fname_matches = Name.objects.filter(fname=dfname)
                lname_matches = Name.objects.filter(lname=dlname)
                if fname_matches and lname_matches:
                    message = f"Multiple names found with first name '{dfname}' or last name '{dlname}', but no exact match."
                elif fname_matches:
                    message = f"Name(s) with first name '{dfname}' found, but last name doesn't match."
                elif lname_matches:
                    message = f"Name(s) with last name '{dlname}' found, but first name doesn't match."
                else:
                    message = "Name not found"

        except Exception as e:
            message = f"An error occurred: {e}"
        # return redirect('contact')
        return render(request, 'contact.html', {'message': message})

from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .serializer import Todo_serializer

@api_view(['GET'])
def get_home(request):
    if request.method =="GET":
        return Response({
            'status' : 200,
            'Message': 'Yes It"s" works!'
        })

@api_view(['POST'])
def todo_post(request):
    # if request.method =="POST":
        try:
            data = request.data
            serializer = Todo_serializer(data = data)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)
                return Response({
                'status' : True,
                'Message': 'Success Data',
                'data' : serializer.data
            })


            return Response({
                'status' : False,
                'Message': 'invaild Data',
                'data' : serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status' : False,
                'Message': 'Didnt works!'
            })
        


@api_view(['GET'])
def get_todo(request):
    todoobj = Todo.objects.all()
    serialiser = Todo_serializer(todoobj, many = True)
    return Response({
        'status ': True,
        'message' : 'Todod fetched',
        'Data' : serialiser.data
    })

@api_view(['PATCH'])
def update(request):
    data = request.data
    if not data.get('uid'):
        return Response({
            'status': False,
            'message': 'UID required',
            'Data': {}
        })

    try:
        obj = Todo.objects.get(uid=data.get('uid'))
        serializer = Todo_serializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Updated',
                'Data': serializer.data
            })
        return Response({
            'status': False,
            'message': 'Invalid Data',
            'Data': serializer.errors
        })
    except Todo.DoesNotExist:
        return Response({
            'status': False,
            'message': 'Invalid UID',
            'Data': {}
        })
    except Exception as e:
        print(e)
        return Response({
            'status': False,
            'message': 'An error occurred. Please try again later.',
            'Data': {}
        }, status=500)
    



def saveform(request):
    if request.method == "POST":
        nid= request.POST.get('id')
        nm = request.POST.get('Name')
        mail= request.POST.get('email')
        Add = request.POST.get('Address')
        Dis = request.POST.get('Description')
        data = Contacts(cid= nid, name = nm, email = mail, add = Add, dis = Dis)
        data.save()
        return redirect('form')
        
def upform(request):
    if request.method == "POST":
        nid= request.POST.get('id')
        nm = request.POST.get('Name')
        mail= request.POST.get('email')
        Add = request.POST.get('Address')
        Dis = request.POST.get('Description')
        obj = Contacts.objects.filter(cid = nid).update(name = nm, email = mail, add = Add, dis = Dis)
        return redirect('home')
        

    

def delformconatct(request):
    id = request.POST.get('id')
    data = Contacts.objects.get(cid=id)
    data.delete()
    return redirect('home')

def Updateconatct(request):
    id = request.POST.get('id')
    obj = Contacts.objects.filter(cid=id)
    context = {'data': obj}
    return render(request, 'form.html', context)