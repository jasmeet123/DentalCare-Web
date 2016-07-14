
from allauth.socialaccount.models import SocialLogin, SocialToken,SocialApp
from allauth.socialaccount.providers.facebook.views import fb_complete_login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.views import APIView

from .models import UserLogin
from .serializer import UserLoginSerializer


class FacebookLoginOrSignup(APIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    @csrf_exempt
    def post(self, Request):
        serializer = UserLoginSerializer(data=Request.data)
        if serializer.is_valid():
            request_data = serializer.data
            userId = request_data.get('fbuserId','')
            access_token = Request.data.get('access_token','')
            try:
                app = SocialApp.objects.get(provider="facebook")
                token = SocialToken(app=app,token=access_token)
                login = fb_complete_login(Request, app, token)
                login.token = token
                login.state = SocialLogin.state_from_request(Request)
                user = UserLogin.objects.all().filter(fbuserId = userId)
                # ret = complete_social_login(Request, login)

                if len(user) == 0:
                    serializer.save()
                    return Response(status=200 ,data={
                         'success': True,
                         'reason': "User created",
                    })
                else:
                    return Response(status=200 ,data={
                         'success': False,
                         'reason': "User already exist",
                     })
            except Exception,e:
                  return Response(status=400 ,data={
                         'success': False,
                         'reason':e,
                     })




    @csrf_exempt
    def get(self,request):
        users = UserLogin.objects.all()
        serializer = UserLoginSerializer(users, many=True)
        return Response(serializer.data)


class UserLogout (APIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    @csrf_exempt
    def get(self, request):
        id =  self.request.query_params.get('id', 100)
        user = UserLogin.objects.get(fbuserId=id)
        user.enable = False
        user.save()
        return Response(status=200 ,data={
                         'success': False,
                         'reason': "User Logged out",
                     })

            # request_data = serializer.data
            # userId = request_data.get('fbuserId','')
            # user = UserLogin.objects.all().filter(fbuserId = userId)
            # if(len(user) == 0):
            #     return Response(status=200 ,data={
            #              'success': False,
            #              'reason': "User does not exist",
            #         })
            #
            # serializer.save()
            # return Response(status=200 ,data={
            #              'success': True,
            #              'reason': "User logged out",
            #         })







    # def post(self, serializer):
    #     serializer.save(owner=self.request.user)



    # def dispatch(self, request, *args, **kwargs):
    #     return  super(FacebookLoginOrSignup, self).dispatch(*args,**kwargs)

    # @csrf_exempt
    # def post(self, request):
    #     data = JSONParser().parse(request)
    #     response = Response()
    #     access_token = data.get('access_token','')
    #
    #     try:
    #         app = SocialApp.objects.get(provider="facebook")
    #         token = SocialToken(app=app,token=access_token)
    #
    #         #check token against facebook
    #         login = fb_complete_login(request, app, token)
    #         login.token = token
    #         login.state = SocialLogin.state_from_request(request)
    #
    #         # add or update the user into usertable
    #         ret = complete_social_login(request,login)
    #
    #         response['Auth-Response'] = 'success'
    #         response.status_code = 200 # Set status
    #         return response
    #     except Exception,e:
    #         # If we get here we've failed
    #         # response['Auth-Response'] = 'failure: %s'%(e)
    #         response.status_code = 401 # Set status
    #         return response
    #     except:
    #         return Response(status=401 ,data={
    #             'success': False,
    #             'reason': "Bad  Token",
    #         })
    #
