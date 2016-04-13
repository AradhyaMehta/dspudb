from __future__ import unicode_literals
from fernet_fields import EncryptedIntegerField, EncryptedCharField, EncryptedDateField
from django.db import models

# Create your models here.
class University(models.Model):
    UniversityId = models.IntegerField(primary_key=True)
    UniversityName = models.CharField(max_length=45)
    UniversityAddress = models.CharField(max_length=75)
    FormationDate = models.DateField()

    def __unicode__(self):
        return self.UniversityName

    class Meta:
        db_table='university'

class Department(models.Model):
    DepartmentId = models.IntegerField(primary_key=True)
    DepartmentName = models.CharField(max_length=45)
    DepartmentHead = models.CharField(max_length=45)
    DepartmentPhone = models.IntegerField()
    UnivId = models.ForeignKey(University)

    def __unicode__(self):
        return self.DepartmentName

    class Meta:
        db_table='department'
        unique_together=(("DepartmentId", "DepartmentName"),)

class Student(models.Model):
    #StudentId = EncryptedIntegerField(primary_key=True)
    StudentId = models.IntegerField(primary_key=True)
    StudentName = EncryptedCharField(max_length=1000)
    StudentAddress = EncryptedCharField(max_length=1000)
    Gender = EncryptedCharField(max_length=1000)
    DateOfBirth = EncryptedDateField()
    #StudentName = models.CharField(max_length=45)
    #StudentAddress = models.CharField(max_length=45)
    #Gender = models.CharField(max_length=45)
    #DateOfBirth = models.DateField()
    DeptId = models.ForeignKey(Department)
    UniverseId = models.ForeignKey(University)

    def __unicode__(self):
        return self.StudentName

    class Meta:
        db_table='student'

class Employee(models.Model):
    EmployeeName = EncryptedCharField(max_length=1000)
    EmployeeId = models.IntegerField(primary_key=True)
    EmployeeSSN = EncryptedIntegerField()
    EmployeePosition = EncryptedCharField(max_length=1000)
    EmployeeSalary = EncryptedIntegerField
    DepartId = models.ForeignKey(Department)
    UniId = models.ForeignKey(University)

    def __unicode__(self):
        return self.EmployeeName

    class Meta:
        db_table='employee'
