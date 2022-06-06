import os
from uuid import uuid4

from django.contrib.auth.hashers import make_password
from django.shortcuts import render

from jinstagram.settings import MEDIA_ROOT
from .models import User
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class Join(APIView): #이 코드는 join이라는 함수를 실행하면, get으로 호출했을떄, user의 폴더 템플릿폴더에 있는 join.html을 보여줘라는 의미이다.
    def get(self, request):
        return render(request, "user/join.html")

    def post(self, request):
        # TODO 회원가입
        email= request.data.get('email',None)
        nickname=request.data.get('nickname',None)
        name=request.data.get('name',None)
        password=request.data.get('password',None)

        User.objects.create(email=email,
                            nickname=nickname,
                            name=name,
                            password=make_password(password),
                            profile_image="default_profile.jpg")
        return Response(status=200)

class Login(APIView):
    def get(self, request):
        return render(request, "user/login.html")

    def post(self, request):
        # TODO 로그인
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status=404, data=dict(message="회원정보가 잘못되었습니다."))

        if user.check_password(password):
            # TODO 로그인을 했다. 세션 or 쿠키
            request.session['email'] = email
            return Response(status=200)
        else:
           return Response(status=400, data=dict(message="회원정보가 잘못되었습니다."))


class LogOut(APIView):
           def get(self, request):
               request.session.flush()
               return render(request,"user/login.html")



class UploadProfile(APIView):
    def post(self, request):

        #일단 파일 불러와
        file = request.FILES['file']

        uuid_name = uuid4().hex #이미지에 고유한 id값을 주기 위한 함수
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk) #이 코든느 파일을 읽어서 파일을 만드는 것.

        profile_image = uuid_name #파일 이름을 profile_image라는 필드에 저장한다.
        email=request.data.get('email')

        user=User.objects.filter(email=email).first() #email로 사용자를 찾는다.

        user.profile_image=profile_image #찾은 사용자의 프로필이미지를 우리가 만든 profile_image로 저장한다.
        user.save()

        return Response(status=200)
