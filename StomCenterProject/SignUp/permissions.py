from django.contrib.auth.models import  User
from rest_framework import permissions
from  rest_framework.permissions import SAFE_METHODS

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        group=None
        if isinstance(request.user,User):
            group=request.user.groups.all()[0].name
        if request.method in SAFE_METHODS:
            return True
        if group=='doctor' and request.method=='POST':
            return True
        elif group=='manager' and request.method=='DELETE':
            return True

class DoctorDayPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        group = None
        if isinstance(request.user, User):
            group = request.user.groups.all()[0].name

        if group in ['doctor','manager']:
            if group == 'doctor' and request.method in ['GET','POST','PUT','DELETE']:
                return True
            elif group == 'manager' and request.method == 'DELETE':
                return True
class ClientPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        group=None
        if isinstance(request.user,User):
            group=request.user.groups.all()[0].name
        if request.method in SAFE_METHODS:
            return True
        if group=='client' and request.method=='POST':
            return True
        elif group=='manager' and request.method in ['GET','PUT','DELETE']:
            return True