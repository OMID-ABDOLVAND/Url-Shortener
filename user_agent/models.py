import uuid
from urlshourter.models import UrlModel
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel
from django.db import models

# Create your models here.

class UserAgentModel(DjangoCassandraModel):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    url = columns.Text()
    os = columns.Text()
    browser = columns.Text()
    ip = columns.Text()

