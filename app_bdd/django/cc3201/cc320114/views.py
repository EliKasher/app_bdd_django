from django.shortcuts import render
from django.http import HttpResponse
from cc320114.models import AppKpop
from cc320114.models import AppKpopCompany
from cc320114.models import AppKpopGroup
from django.db import connection
from collections import namedtuple
# action or request handler

def main1(request):
    return render(request, 'main1.html') 

def main2(request):
    return render(request, 'main2.html')

def main3(request):
    return render(request, 'main3.html')

def main4(request):
    return render(request, 'main4.html')

def main5(request):
    return render(request, 'main5.html')
    
def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]
        
def consulta1(request):
    #Pull data from db
    if request.method == 'POST':
        inputs = '%' + request.POST['artista'] + '%'
        query = AppKpop.objects.raw('''SELECT DISTINCT S.id, A.id, S.name AS sname, A.name AS aname
        FROM app_kpop S, app_kpop_group A
        WHERE A.name LIKE %s
        AND A.is_collab = 'y'
        AND S.id_artist = A.id
        ORDER BY S.name ASC''', (inputs,))
    return render(request, 'consulta1.html', {'resultados': query})
    

def consulta2(request):
    #Pull data from db
    if request.method == 'POST':
        inputs = request.POST
        query = AppKpop.objects.raw('''SELECT DISTINCT A1.name AS name1, A2.name AS name2, C.name, C.id
        FROM app_kpop_company C, app_kpop_group A1, app_kpop_group A2
        WHERE C.name = %s 
        AND C.id = A1.id_company
        AND C.id = A2.id_company
        AND A1.name < A2.name
        ORDER BY C.name ASC''', (inputs['company'],))
    return render(request, 'consulta2.html', {'resultados': query})

def consulta3(request):
    #Pull data from db
    if request.method == 'POST':
        inputs = request.POST
        query = AppKpop.objects.raw('''SELECT C.id, C.name AS company, COUNT(DISTINCT(A.id,A.name)) AS number
        FROM app_kpop_group A, app_kpop_company C
        WHERE A.members = %s
        AND A.id_company = C.id
        AND C.name = %s
        GROUP BY C.name, C.id
        ORDER BY C.name ASC''', (inputs['gender'],inputs['company'],))
    return render(request, "consulta3.html", {'resultados': query})

def consulta4(request):
    #Pull data from db
    if request.method == 'POST':
        inputs = request.POST
        query = AppKpop.objects.raw('''SELECT DISTINCT S.id, S.name, S.views
        FROM app_kpop S, app_kpop_group A
        WHERE A.name = %s
        AND S.id_artist = A.id
        GROUP BY S.id, S.name, S.views
        HAVING MIN(S.views) >= %s''', (inputs['artista'],inputs['minimo'],))
    return render(request, "consulta4.html", {'resultados': query})

def consulta5(request):
    #Pull data from db
    if request.method == 'POST':
        inputs = request.POST
        query = AppKpop.objects.raw('''SELECT DISTINCT A2.id, A2.name, A2.yt_followers 
        FROM app_kpop_group A2
        WHERE A2.yt_followers >
           (SELECT DISTINCT A1.yt_followers
           FROM app_kpop_group A1
           WHERE A1.name = %s)
        ORDER BY A2.name, A2.yt_followers DESC''', (inputs['artista'],))
    return render(request, "consulta5.html", {'resultados': query})
    
    