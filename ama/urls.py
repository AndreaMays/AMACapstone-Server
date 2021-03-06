"""ama URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from amaapi.views.awards import AwardViews
from amaapi.views.competitions import CompetitionViews
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from amaapi.views import register_user, login_user
from amaapi.views import LessonNoteView, StudentUserNotesView, StudentUserListView, StudentCompetitionList, AwardsListViews



router = routers.DefaultRouter(trailing_slash=False)

router.register(r'notes', LessonNoteView, 'note')
router.register(r'studentnotes', StudentUserNotesView, 'studentnote')
router.register(r'studentlist', StudentUserListView, 'studentlist')
router.register(r'competitions', CompetitionViews, 'competition')
router.register(r'competitionlists', StudentCompetitionList, 'competitionlist')
router.register(r'awards', AwardViews, 'award')
router.register(r'awardslist', AwardsListViews, 'awardlist')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^register$', register_user),
    path(r'login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
