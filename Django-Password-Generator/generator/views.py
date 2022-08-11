from django.shortcuts import render #   render sirve para leer un archivo y devolverlo al servidor
# from django.http import HttpResponse    Convierte a los strings en respuestas HTTP
import random   #   Este módulo permite agregar valores al azar

def home(request):
    return render(request, 'generator/home.html') #   Renderiza los archivos html y los devuelve al servidor

#   Función para guardar los password
def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz') #   Lista de caracteres
    generate_password = ''  #   Variable donde se almacenará el password
    
    length = int(request.GET.get('length'))   #   esta variable obtiene la longitud del password
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))   #   va a iterar los caracteres a Mayúscula
    if request.GET.get('special'):
        characters.extend(list('!@#$%()/^*+-_'))  #   Lista de  especiales
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))  #   Lista de numeros
        
    #   Recorrer los caracteres
    for i in range(length): #   Recorre la longitud del password gracias a la variable length
        generate_password += random.choice(characters)  
    
    return render(request, 'generator/password.html', {'password': generate_password })