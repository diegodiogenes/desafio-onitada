from users.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create default users'

    def add_arguments(self, parser):
        parser.add_argument('-u', '--username', type=str, help='Define a username', required=True)
        parser.add_argument('-p', '--password', type=str, help='Define a password', required=True)
        parser.add_argument('-e', '--email', type=str, help='Define a email', required=True)
        parser.add_argument('-c', '--cpf', type=str, help='Define a CPF', required=True)

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        email = kwargs['email']
        cpf = kwargs['cpf']
        User.objects.create_user(username=username, email=email, password=password, cpf=cpf)
