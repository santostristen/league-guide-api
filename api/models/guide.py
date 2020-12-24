from django.db import models
from django.contrib.auth import get_user_model


class Guide(models.Model):
  title = models.CharField(max_length=100)
  text = models.CharField(max_length=750)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return self.title

    def as_dict(self):
      return {
        'id': self.id,
        'title': self.title,
        'text': self.text
  }
