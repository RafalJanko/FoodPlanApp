"""scrumlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jedzonko.views import IndexView, RecipesView, AddRecipesView, DashboardView, AddPlanView, RecipeDetailsView, \
    AddRecipeToPlan, PlansView, PlanDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('main', DashboardView.as_view()),
    path('recipe/list', RecipesView.as_view(), name='recipesList'),
    path('recipe/add', AddRecipesView.as_view(), name='recipeAdd'),
    path('main/', DashboardView.as_view()),
    path('plan/list', PlansView.as_view()),
    path('plan/add', AddPlanView.as_view(), name='addPlan'),
    path('plan/add-recipe/', AddRecipeToPlan.as_view()),
    path('recipe/<int:idd>/', RecipeDetailsView.as_view()),
    path('plan/<int:idd>/details', AddRecipeToPlan.as_view()),
    path('plan/<int:idd>', PlanDetailsView.as_view()),

]
