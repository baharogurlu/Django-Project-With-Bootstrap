# Django-Project-With-Bootstrap
Django Project With Bootstrap
Database-URL-Views-Bootstrap Template-Security

My site adlı proje oluştukmak için:
django-admin startproject mysite

Poll adında bir app eklemek için:
python manage.py startapp polls
Uygulamayı çalıştırmak için mysite içerisine gidip:
  python manage.py runserver
Model eklendikten sonra polls app i için :
python manage.py makemigrations polls
mysite içerisindeki settings.py içerisine INSTALLED_APPS Altına ‘polls’, ifadesi eklenir. Bu işlemden sonra 
1-)python manage.py makemigrations polls
2-)python manage.py migrate
 komutu çalıştırılır. Migrations dosyası içerisinde initial.py adlı file oluşur. Bu file içerisinde oluşturduğunuz modeller gözükür.

POPULATING DATABASE:
1.	python manage.py Shell
2.	>>> import django
3.	>>> django.setup()
4.	>>> from polls.models import Question,Choice
5.	Question.objects.all()
6.	from django.utils import timezone
7.	>>> q=Question(question_text="whats your name",pub_date=timezone.now())
8.	>>> q.save()
9.	>>> Question.objects.all()
10.	exit()

Models.py içerisine 
def __str__(self):
 return self.choice_text


modeller içerisindeki değerleri döndüren metod yazılır. Choice_text bi attributre tır.

python manage.py createsuperuser //süper user oluşturma
python manage.py runserver

