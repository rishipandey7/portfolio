from django.urls import path

from main import views

urlpatterns = [
     path('projects/',views.projects, name="projects"),
     path('languages/',views.languages, name="languages"),
     path('skills/',views.skills, name="skills"),
     path('skills/logicstrength',views.logicstrength, name="logicstrength"),
     path('skills/logiccourses',views.logiccourses, name="logiccourses"),
     path('skills/programmingstrength',views.programmingstrength, name="programmingstrength"),
     path('skills/programmingcourses',views.programmingcourses, name="programmingcourses"),
     path('skills/technicalstrength',views.technicalstrength, name="technicalstrength"),
     path('skills/technicalcourses',views.technicalcourses, name="technicalcourses"),
     path('skills/communicationstrength',views.communicationstrength,name ="communicationstrength"),
     path('skills/communicationcourses',views.communicationcourses,name="communicationcourses"),
     
     
     
     

     
     path('',views.index, name="index")

]
