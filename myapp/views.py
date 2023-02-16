from django.shortcuts import render, redirect
from myapp.models import Person
import boto3
import os
import uuid
import logging


# dynamodb = boto3.resource('dynamodb')
dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='AKIA3KDHEOPJW576CEP6',
    aws_secret_access_key='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',
    region_name='ap-south-1'
)

table = dynamodb.Table('Person')

def read_person(request):
    

    # val = 'test5'
    # # response = Person.get_person('test5')
    # response = table.get_item({'email':'test5'})
    # item = response.get('Item')
    # items = Person.objects.all()
    # return render(request, 'index.html', {'items': item})
    if request.method == 'GET':
        response = table.scan()
        item = response['Items']

        # response = table.get_item(Key={
        #         'first_name': 'test5'
        #     })
        # item = response['Item']

        # response = Person.get_person('test5')
        # return redirect('/')
        return render(request, 'read.html',{'items': item}) 
    return redirect('/')

def create_person(request):
    if request.method == 'POST':
        id = str(uuid.uuid1())
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        # id = request.POST.get('id')
        person = Person(first_name=first_name, last_name=last_name, email=email,id=id)
        person.save()
        # person.get_person()
        return redirect('/')
    logging.info("root")
    # logging.log("INFO","root")
    logging.error('error')
    return render(request, 'create.html')

def update_person(request):
    # person = Person.get_person(email_id)
    if request.method == 'POST':
        response = table.scan()
        item = response['Items']
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_id = request.POST.get('email')
        id = request.POST.get('id')
        Person.update_person1(id,email_id,first_name,last_name)
        return redirect('/')
    return render(request, 'update.html')


def delete_person(request):
    # person = Person.get_person(email_id)
    if request.method == 'POST':
        response = table.scan()
        item = response['Items']
        id = request.POST.get('id')

        Person.delete_person1(id)
        return redirect('/')
    return render(request, 'delete.html')



    # if request.method == 'POST':
    #     for i in item:
    #         if i['email'] == email_id:
    #             first_name = request.POST.get('first_name')
    #             last_name = request.POST.get('last_name')
    #             email = i['email']
    #             id = i['id']
    #             person = Person(first_name=first_name, last_name=last_name, email=email,id=id)
    #             person.save()
    #             # item['first_name'].update(first_name=first_name, last_name=last_name)
    #     return redirect('read')
    # return render(request, 'update.html', {'person': person})

# def update_person(request, person_id):
#     if request.method == 'POST':
#         # code to handle the update operation goes here
#         return redirect('/')
#     return render(request, 'update.html', {'person': person})









