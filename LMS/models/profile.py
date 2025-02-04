from django.db import models
from phnuser import Phnuser

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('adult', 'Adult'),
    ]

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    name = models.CharField(max_length=100)
    username = models.ForeignKey(Phnuser,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    dob = models.DateField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    # Fields specific to students
    school = models.CharField(max_length=100, blank=True, null=True)
    grade = models.CharField(max_length=50, blank=True, null=True)
    student_id = models.CharField(max_length=50, blank=True, null=True)
    guardian = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact = models.CharField(max_length=15, blank=True, null=True)

    # Fields specific to adults
    occupation = models.CharField(max_length=100, blank=True, null=True)
    workplace = models.CharField(max_length=100, blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    work_address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
