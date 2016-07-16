from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Import the email modules we'll need

from django.views.decorators.csrf import csrf_exempt
from .models import Request
from .serializer import UserRequestSerializer
from rest_framework import status
from zipcode_distance import distance
from dentist_login.models import Dentist
from UserLogin.models import UserLogin

# Create your views here.

class UserRequest(APIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    @csrf_exempt
    def post(self, request):
        serializer = UserRequestSerializer(data=request.data)
        if serializer.is_valid():

            data = serializer.data
            title =  data.get("request_title",'')
            desc = data.get('request_desc','')
            user_email = data.get('request_user','')

            send_email = self.get_dentist(user_email,serializer)
            serializer.save()
            if send_email != "":
                self.sendEmail(title,desc,send_email)


            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @csrf_exempt
    def get(self, request):
        id =  self.request.query_params.get('id', '')
        user = UserLogin.objects.get(fbuserId=id)
        user_requests = Request.objects.all().filter(request_user=user.email)
        return Response(user_requests, status=status.HTTP_201_CREATED)



    def get_dentist(self, email,serializer):
        dentist = Dentist.objects.all()
        user = UserLogin.objects.get(email=email)
        user_dentist = user.user_dentist
        if user_dentist != None:
            return user.user_dentist.email
        if user != None:
            count = dentist.count()
            user_zip = user.zip
            i = 0
            while i < count:
                i = i+1
                dentist_item = dentist[i]
                dentist_zip = dentist_item.zip
                dist = self.checkDistance(dentist_zip,user_zip)
                if(dist > 50):
                    pass
                else:
                    dentist_email = dentist_item.email
                    user.user_dentist = dentist_item
                    serializer.validated_data['request_dentist'] = dentist_item
                    user.save()

                    return dentist_email

        return ""


    @csrf_exempt
    def get(self,request,format=None):
        requests = Request.objects.all()
        serializer = UserRequestSerializer(requests, many=True)
        return Response(serializer.data)

    def checkDistance(self, user_zip, dentist_zip):
        return distance(user_zip,dentist_zip)



    def sendEmail(self,title,desc,user_email):
        from_email = 'jasmeet.manak@gmail.com'
        send_mail(title, desc, from_email,[user_email],
     fail_silently=True)
        # msg = MIMEMultipart()
        # msg['Subject'] = 'Hello'
        # myAddress = 'jasmeet.androiddev@gmail.com'
        # toAddress = 'jasmeet.manak@gmail.com'
        # msg['From'] = myAddress
        # msg['To'] = toAddress
        # msg.preamble = 'JAzz'
        # s = smtplib.SMTP('localhost')
        # s.sendmail(myAddress,toAddress,msg.as_string())
        # s.quit()



















