from django.db import models
from boto3 import resource
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Person')

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    id = models.CharField(primary_key=True,max_length=10)

    def save(self, *args, **kwargs):
        table.put_item(
            Item={
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'id': self.id
            }
        )
        super(Person, self).save(*args, **kwargs)

    @classmethod
    def get_person(cls, email):
        response = table.get_item(
            Key={
                email: email
            }
        )
        item = response.get('Item')
        return cls(first_name=item['first_name'], last_name=item['last_name'], email=item['email'],id = id['id'])

    @classmethod
    def delete_person1(cls, id):
        table.delete_item(
            Key={
                'id': id
            }
        )
    @classmethod
    def update_person1(cls,id, email, first_name, last_name):
        response = table.update_item(
        Key={
            'id': id
        },
        UpdateExpression='SET first_name = :first_name, last_name = :last_name, email = :email',
        ExpressionAttributeValues={
            ':first_name': first_name,
            ':last_name': last_name,
            ':email':email
        })
        return response
