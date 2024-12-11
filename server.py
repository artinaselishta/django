pip install django
django-admin startproject gjykata
cd gjykata
python manage.py startapp gjykata_app

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gjykata_db',
        'USER': 'admin',
        'PASSWORD': 'password123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

from django.db import models

class Përdorues(models.Model):
    emër = models.CharField(max_length=100)
    mbiemër = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    roli = models.CharField(max_length=50, choices=[('gjykatës', 'Gjykatës'), ('avokat', 'Avokat'), ('qytetar', 'Qytetar')])
    
class SeancaGjyqësore(models.Model):
    titulli = models.CharField(max_length=255)
    data = models.DateField()
    gjykatës = models.ForeignKey(Përdorues, on_delete=models.CASCADE, related_name='gjykates_seanca')
    dokumentet = models.FileField(upload_to='dokumentet/')

from django.http import JsonResponse
from .models import Përdorues, SeancaGjyqësore

def lista_seancave(request):
    seancat = SeancaGjyqësore.objects.all().values()
    return JsonResponse(list(seancat), safe=False)

pip install djangorestframework

pip install flask flask-sqlalchemy flask-jwt-extended

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gjykata.db'
db = SQLAlchemy(app)

class Perdorues(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emër = db.Column(db.String(100))
    mbiemër = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    roli = db.Column(db.String(50))

@app.route('/seancat', methods=['GET'])
def lista_seancave():
    return jsonify({"mesazhi": "Kjo është një listë e seancave."})

if __name__ == '__main__':
    app.run(debug=True)
