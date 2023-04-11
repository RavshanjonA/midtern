import uuid

from django.utils import timezone


def service_logo_upload_path(instance, filename):
    current_dt = timezone.now()
    return f'service/{current_dt.strftime("%Y_%m")}/{uuid.uuid4().hex}/{filename}'

def avatar_upload_path(instance, filename):
    current_dt = timezone.now()
    return f'service/{current_dt.strftime("%Y_%m")}/{uuid.uuid4().hex}/{filename}'
