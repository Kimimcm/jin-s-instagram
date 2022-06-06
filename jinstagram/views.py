from django.shortcuts import render
from rest_framework.views import APIView #장고 framework를 설치한 이유이다. 이 패키지 안에 aipview 함수가 있는데 이 함수가 rest를 호출할 수 있도록 도와준다. 즉, get 혹은  post을 호출할 수 있도록 해줌.


class Sub(APIView):
    def get(self, request):
        print("겟으로 호출")
        return render(request, "jinstagram/main.html")

    def post(self, request):
        print("포스트로 호출")
        return render(request, "jinstagram/main.html")
