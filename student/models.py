from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    status = models.CharField(
        max_length=100,
        choices=(("approved", "Approved"), ("disapproved", "Disapproved")),
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def name(self):
        return f"{self.first_name} {self.last_name}"


class Document(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    obj = models.FileField(upload_to="students/", verbose_name="File")

    def __str__(self):
        return f"{self.student}'s file"
