from django.db import models
from django.utils import timezone

class Registration(models.Model):
    AIESECER_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    SOURCE_CHOICES = [
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('LinkedIn', 'LinkedIn'),
        ('Twitter/X', 'Twitter/X'),
        ('TikTok', 'TikTok'),
        ('Email Newsletter', 'Email Newsletter'),
        ('Friend', 'Friend'),
        ('AIESEC Member', 'AIESEC Member'),
        ('Other', 'Other'),
    ]

    full_name = models.CharField(max_length=255, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    university = models.CharField(max_length=255, blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    is_aiesecer = models.CharField(max_length=3, choices=AIESECER_CHOICES, blank=True, null=True)
    topics_interested = models.TextField(blank=True, null=True)
    how_did_you_hear = models.CharField(max_length=50, choices=SOURCE_CHOICES, blank=True, null=True)
    promo = models.TextField(blank=True, null=True)

    # ✅ TEMPORARY: Allow NULL for Migration Step
    timestamp = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.full_name if self.full_name else "No Name Provided"
