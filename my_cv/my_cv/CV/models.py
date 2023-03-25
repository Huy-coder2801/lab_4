from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class Education(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class Experience(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

