from rest_framework import authentication
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView

from permissions import isOwnerOrReadOnly
from .models import Tip
from .serializer import TipsSerializer


class TipViewSet(ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,isOwnerOrReadOnly)
    queryset = Tip.objects.all().order_by('-date')
    serializer_class = TipsSerializer


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # @detail_route(methods='post')
    # def get_queryset(self):
    #     queryset = Tips.objects.all()
    #     date = self.kwargs['date']
    #     if(date is not None):
    #        set =  queryset.filter(date=date)
    #     return set



class TipTodayList(ListCreateAPIView):
    serializer_class = TipsSerializer


    def get_queryset(self):
        queryset = Tip.objects.all()
        date = self.kwargs['date']
        if(date is not None):
           set =  queryset.filter(date=date)
        return set


class TipDetail(RetrieveUpdateAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,isOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)




# Create your views here.
