
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from .serializer import DentistSerializer
from .models import Dentist
import json
from rest_framework.authtoken.models import Token
from UserRequest.zipcode_distance import distance
from UserLogin.models import UserLogin



class DentistView(APIView):

    authentication_classes = (authentication.TokenAuthentication, authentication.BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    # def dispatch(self, request, *args, **kwargs):
    #     return  super(FacebookLoginOrSignup, self).dispatch(*args,**kwargs)

    @csrf_exempt
    def post(self, request):
        data = JSONParser().parse(request)
        response = Response()
        email = data.get('email','')
        password = data.get('password','')

        try:
            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_active:


                  return Response(status=200, data={

                      'success': True,
                      'id':user.id,
                      'first_name':user.first_name,
                      'last_name':user.last_name,
                      'email':user.email,
                      'address':user.address,
                      'city':user.city,
                      'state':user.state,





                  })
                else:
                     return Response(status=401, data={
                      'success': False,
                      'reason' : "Please check password"
                  })

            else:
                     return Response(status=401, data={
                      'success': False,
                      'reason' : "User does not exist"
                  })

        except Exception,e:

           return Response(status=401, data={
                      'success': False,
                      'reason' : e
                  })
        except:
            return Response(status=401 ,data={
                'success': False,
                'reason': "Bad  Token",
            })



    @csrf_exempt
    def get(self,request):
        users = Dentist.objects.all()
        serializer = DentistSerializer(users, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def get(self,request):
       dentist = Dentist.objects.all().values()
       id = self.request.query_params.get('id', None)
       if(id == None):
            return Response(status=200, data={
                      'success': True,
                      'data' : dentist
                 })
       radius =  self.request.query_params.get('radius', 100)
       user = UserLogin.objects.get(fbuserId=id)
       dentist_array = [];
       if user != None:
            count = dentist.count()
            user_zip = user.zip
            i = 0
            while i < count:
                dentist_item = dentist[i]
                dentist_zip = dentist_item.get('zip')
                dist = distance(dentist_zip,user_zip)
                if(dist < int(radius) and dentist_item.get('active') == True):
                   dentist_array.append(dentist_item)
                else:
                    pass
                i = i+1

       return Response(status=200, data={
                      'success': True,
                      'data' : dentist_array
                  })



    def token_request(self, Dentist):
        return Token.objects.get_or_create(user=Dentist)





