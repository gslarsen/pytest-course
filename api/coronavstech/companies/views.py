from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination


@api_view(http_method_names=["POST"])
def send_company_email(request):
    """
    sends email with request payload
    sender: glarsen8172@gmail.com
    receiver: glarsen8172@gmail.com
    """

    send_mail(
        subject="My cool subject",
        message="My cool msg",
        from_email="glarsen8172@gmail.com",
        recipient_list=["glarsen8172@gmail.com"],
    )
    return Response(
        {"status": "success", "info": "email sent successfully"}, status=200
    )
