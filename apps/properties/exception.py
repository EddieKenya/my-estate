from rest_framework.exceptions import APIException

class PropertyNotFound(APIException):
    status_code = 404
    default_detail = "Sorry! Property does not exist!"


