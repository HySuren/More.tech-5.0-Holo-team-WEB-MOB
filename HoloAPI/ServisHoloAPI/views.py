import psycopg2
from django.http import HttpResponse
from psycopg2 import Error
import json
from ServisHoloAPI.distance import DistanceMap
from geopy.distance import great_circle
import random
from pathlib import Path
import os
from read import config_data

BASE_DIR = Path(__file__).resolve().parent.parent

class UserRepository:

    def register_user(self, email, password):
        connect = psycopg2.connect(f"dbname={config_data.NAME} user={config_data.USER} password={config_data.PASSWORD}")
        try:
            cursor = connect.cursor()
            cursor.execute(f"""INSERT INTO "User"(login,email, password)VALUES('ed','{email}','{password}');""")
            connect.commit()

            cursor.close()
            return True
        except (Exception, Error) as error:
            return error
        finally:
            cursor.close()

    def authenticate_user(self, email, password):
        connect = psycopg2.connect(f"dbname={config_data.NAME} user={config_data.USER} password={config_data.PASSWORD}")
        try:
            cursor = connect.cursor()
            cursor.execute(f"""SELECT email,password FROM "User" WHERE email='{email}' AND password='{password}'""")
            connect.commit()
            cursor.close()
            return True
        except (Exception, Error) as error:
            return error
        finally:
            cursor.close()


class RegistrationView:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def registration(self, request):
        json_error_message = {
            'message': '401',
        }
        json_successfully_message = {
            'message': '200',
        }
        email = request.POST.get("email")
        password = request.POST.get("password")
        if self.user_repository.register_user(email, password):
            data = json.dumps(json_successfully_message)
        else:
            data = json.dumps(json_error_message)
        return HttpResponse(data, content_type='application/json')


class AuthorizationView:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def authorization(self, request):
        json_error_message = {
            'message': '401',
        }
        json_successfully_message = {
            'message': '200',
        }
        if True:
            email = request.GET.get("email")
            password = request.GET.get("password")
            if user_repository.authenticate_user(email, password):
                data_1 = json.dumps(json_successfully_message)
                return HttpResponse(data_1, content_type='application/json')
            else:
                data_2 = json.dumps(json_error_message)
            return HttpResponse(data_2, content_type='application/json')


class DistanceView:
    def distance(self, request):
        location = {}
        latitude = request.GET.get("latitude")
        longitude = request.GET.get("longitude")
        geoposition = (latitude, longitude)
        with open(os.path.join(BASE_DIR,'ServisHoloAPI','offices_pep.json'), 'r') as json_file:
            data = json.loads(json_file.read())
        for item in data:
            try:
                address = DistanceMap.geocode_address(item)
            except:
                continue
            distance = great_circle(geoposition, address).m
            location["location"] = [address, distance]
        return HttpResponse(sorted(location.items(), key=lambda item: item[1]), content_type='application/json')


class WorkloadView:
    def workload(self):
        talons = random.randint(0, 50)
        avg_time = random.randint(120, 600)
        sumary_work = random.randint(10, 15)
        result = talons * 10 / avg_time * sumary_work
        data = {'procent': result}
        response_json = json.dumps(data)
        return HttpResponse(response_json, content_type='application/json')


user_repository = UserRepository()
registration_view = RegistrationView(user_repository)
authorization_view = AuthorizationView(user_repository)
distance_view = DistanceView()
workload_view = WorkloadView()