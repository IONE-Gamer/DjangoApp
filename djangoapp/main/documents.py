from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Task

@registry.register_document
class TaskDocument(Document):
    class Index:
        name = 'task'    
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }    
    class Django:
         model = Task         
         fields = [
             'title',
             'task',
         ]