from django.db import models
from users.models import User

# Create your models here.


class PDocs(models.Model):
    docs=models.FileField(upload_to='files')
    owner = models.ForeignKey(User, related_name ='owner_docs', on_delete=models.CASCADE, default='owner doc')

    def __str__(self):
        return self.owner
