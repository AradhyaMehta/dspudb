from __future__ import unicode_literals

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
    StudentId = models.IntegerField(primary_key=True)
    StudentName = models.CharField(max_length=45)
    StudentAddress = models.CharField(max_length=45)
    Gender = models.CharField(max_length=45)
    DateOfBirth = models.DateField()
    DeptId = models.ForeignKey(Department)
    UniverseId = models.ForeignKey(University)

    def __unicode__(self):
        return self.StudentName

    class Meta:
        db_table='student'

class Employee(models.Model):
    EmployeeName = models.CharField(max_length=45)
    EmployeeId = models.IntegerField(primary_key=True)
    EmployeeSSN = models.IntegerField()
    EmployeePosition = models.CharField(max_length=45)
    EmployeeSalary = models.IntegerField()
    DepartId = models.ForeignKey(Department)
    UniId = models.ForeignKey(University)

    def __unicode__(self):
        return self.EmployeeName

    class Meta:
        db_table='employee'
