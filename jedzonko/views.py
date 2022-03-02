from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, redirect

from django.urls import reverse

from django.views import View
from jedzonko.models import Recipe, Plan, RecipePlan
from random import shuffle



class IndexView(View):
    def get(self, request):

        recipes_desc = [(x.description, x.name) for x in Recipe.objects.all()]
        shuffle(recipes_desc)
        recip1 = recipes_desc[0]
        recip2 = recipes_desc[1]
        recip3 = recipes_desc[2]
        print(recip1)
        return render(request, "index.html", {
            "recip1_name":recip1[1], 
            "recip2_name":recip2[1], 
            "recip3_name":recip3[1],
            "recip1_desc":recip1[0], 
            "recip2_desc":recip2[0], 
            "recip3_desc":recip3[0],
            })


class AddRecipesView(View):
    def get(self, request):
        
        return render(request, "app-add-recipe.html")

    def post(self, request):
        # zbieranie info z formularza
        name = request.POST.get("r_name")
        description = request.POST.get("description")
        time = int(request.POST.get("time"))
        preparing = request.POST.get("preparing")
        ingredient = request.POST.get("ingredient")

        # dodanie przepisu do bazy danych 
        Recipe.objects.create(
                name=name, 
                description=description, 
                ingredients=ingredient, 
                preparation_time=time, 
                preparing=preparing,
                votes=0,
                ) 

        return redirect("recipeAdd")


class AddPlanView(View):
    def get(self, request):
        return render(request, "app-add-schedules.html")


class AddRecipeToPlan(View):
    def get(self, request):

        return render(request, "app-schedules-meal-recipe.html")


class DashboardView(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        plans = Plan.objects.all()
        plans_count = plans.count()
        recipes_count = recipes.count()

        return render(request, "dashboard.html", {'plans_count':plans_count, 'recipes_count':recipes_count})

class RecipesView(View):

    def get(self, request):

        recipes = Recipe.objects.all()
        count = recipes.count()

        return render(request, "app-recipes.html", {'recipes':recipes, 'count':count})

class RecipeDetailsView(View):
    def get(self,request,idd):
        recipe_details = Recipe.objects.get(id=idd)
        return render(request, 'app-recipe-details.html', {'recipe_details': recipe_details})

    def post(self, request, idd):
        recipe_details = Recipe.objects.get(id=idd)
        votes = recipe_details.votes
        if 'lubie' in request.POST:
            new_votes = int(votes) + 1
            recipe_details.votes = new_votes
            recipe_details.save()
        elif 'nie_lubie' in request.POST:
            new_votes = int(votes) - 1
            recipe_details.votes = new_votes
            recipe_details.save()

        return render(request, 'app-recipe-details.html', {'recipe_details': recipe_details})

class PlansView(View):
    def get(self, request):

        pl = Plan.objects.all()
        paginator = Paginator(pl, 50)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, "app-schedules.html", {'pl':pl, 'page_obj':page_obj})

class AddPlanView(View):
    def get(self, request):
        return render(request, "app-add-schedules.html")

    def post(self, request):

            plan_name = request.POST.get('planName')
            plan_description = request.POST.get('planDescription')
            if plan_name and plan_description:

                p=Plan.objects.create(name=plan_name, description=plan_description)
                idd=p.id

            else:
                return HttpResponse('wypełnij wszystkie pola')


            return redirect(reverse(f'(plan/{idd}/details)'))


class PlanDetailsView(View):
    def get(self,request,idd):
         plan_details = Plan.objects.get(id=idd)
         return render(request, 'app-details-schedules.html', {'plan_details':plan_details})


