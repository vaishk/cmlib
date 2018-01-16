# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
# Create your models here.

class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField('ISBN',max_length=13)
    categories = models.ManyToManyField('Categories')
    borrowed_by = models.ForeignKey('Borrower', null=True, blank=True)
    borrowed_till = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
        

class Categories(models.Model):
    """
    Model representing keywords as categories 
    """
    name = models.CharField(max_length=200)
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Borrower(models.Model):
	"""
    Model for borrowers 
    """
	name= models.CharField(max_length=100)

	def __str__(self):
		return self.name






