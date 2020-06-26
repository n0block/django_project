from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Classification(models.Model):
    classification_name = models.CharField(max_length=100)

    def __str__(self):
        return self.classification_name


class Submission(models.Model):
    title = models.CharField(max_length=200)
    product_name = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=100)
    description_text = models.TextField()
    submission_date = models.DateTimeField(default=timezone.now)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse('submission-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.product_name
