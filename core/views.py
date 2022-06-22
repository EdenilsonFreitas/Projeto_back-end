from django.shortcuts import render
from django.http import HttpResponse

def olamundo(request):
    return HttpResponse('<h1>olá Mundo</h1>')
def Disciplina(request):
    return HttpResponse('<p>Back End</p>')
def home(request):
    return HttpResponse('<h1>Página Inicial</h1>') 
def minha_idade(request,idade):
    return HttpResponse('A idade digitada é' + str(idade))   
def meu_nome(request,nome):
    return HttpResponse("O nome é: " +nome)
def minha_nota(request,nota):
    dobro = 2* float(nota)
    return HttpResponse('Dobro da nota: ' +str(dobro))  
def cadastro(request,nome,idade):
    return HttpResponse('Nome: ' + nome+"e Idade: " +str(idade))   
def pag1(request):
    return HttpResponse('<a href="/Pagina2/" >Pagina 2</a>')   

def pag2(request):
    return HttpResponse('<a href="/Pagina1">Pagina 1</a>')   

def teste(request):
    return render(request, 'teste.html')



