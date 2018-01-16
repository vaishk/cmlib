# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

from .models import Book

class index(ListView):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    model = Book
    context_object_name = 'all_books'
    template_name = 'index.html'