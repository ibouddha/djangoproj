from django.http import HttpResponse, JsonResponse
from .models import Article
import json
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def accueil(request):
    results = Article.get_all()
    articles = [dict(row._asdict()) for row in results]
    # print(articles,end="\n")
    return render(request,'index.html',{'articles':articles})


@csrf_exempt
def create(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            data = request
            
            titre = data.POST.get('titre')
            contenu = data.POST.get('contenu')
            
            if titre and contenu:
                # Process the data (e.g., save to the database)
                Article.save(titre, contenu)
                
                return redirect('/')
            else:
                return JsonResponse({"error": "Missing fields"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)
    
@csrf_exempt
def update(request, id):
    if request.method == 'PUT':
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)
            
            titre = data.get('titre')
            contenu = data.get('contenu')
            
            if titre and contenu:
                # Process the data (e.g., save to the database)
                Article.update(id, titre, contenu)
                
                return JsonResponse({"message": "Article updated successfully"}, status=200)
            else:
                return JsonResponse({"error": "Missing fields"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)
    
@csrf_exempt
def delete(request, id):
    if request.method == 'GET':
        try:
            # Process the data (e.g., save to the database)
            Article.delete(id)
            
            return redirect('/')
        except:
            return JsonResponse({"error": "Failed to delete article"}, status=500)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)