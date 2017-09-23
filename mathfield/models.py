# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json
import six

import django
from django.db import models
from django.core import exceptions
from mathfield.api import store_math

if six.PY3:
    basestring = str


MathFieldValidationError = lambda self, value: exceptions.ValidationError(
    'Could not resolve "{0}" to a dictionary with only keys "raw" and "html"'
    .format(str(value)))


class MathField(models.TextField):

    description = 'Field that allows you to write LaTeX and display it as HTML.'

    if six.PY2 and django.VERSION <= (1, 7):
        __metaclass__ = models.SubfieldBase

    def from_db_value(self, value, expression, connection, context):
        """'to_python like' behaviour for Django > 1.8."""
        return self.to_python(value)

    def to_python(self, value):
        """ The data is serialized as JSON with the keys `raw` and `html` where
            `raw` is the entered string with LaTeX and `html` is the html string
            generated by KaTeX. If this function gets just a string,
            then we need to generate the LaTeX.

            WARNING: Generating the LaTeX server-side requires Node.js to be
            installed. To generate the LaTeX client-side, make sure that you
            specify that the MathFields that you use are assigned to the widget
            `MathFieldWidget` in your app's admin.py.
        """
        if value is None:
            return None

        if value == "":
            return {'raw': '', 'html': ''}

        if isinstance(value, basestring):
            try:
                return dict(json.loads(value))
            except (ValueError, TypeError):
                return {'raw': value, 'html': ''}

        if isinstance(value, dict):
            return value

        return {'raw': '', 'html': ''}

    def get_prep_value(self, value):
        if not value:
            return json.dumps({'raw': '', 'html': ''})

        if isinstance(value, basestring):
            try:
                dictval = json.loads(value)
            except (ValueError, TypeError):
                return json.dumps({'raw': value, 'html': ''})
            else:
                if {'raw', 'html'} == set(dictval.keys()):
                    return value
                else:
                    raise MathFieldValidationError(self, value)

        if isinstance(value, dict):
            if {'raw', 'html'} == set(value.keys()):
                return json.dumps(value)
            else:
                raise MathFieldValidationError(self, value)

        return json.dumps({'raw': '', 'html': ''})

    def formfield(self, **kwargs):
        defaults = {
            'help_text': ('Type text as you would normally, or write LaTeX '
                          'by surrounding it with $ characters.')
        }
        defaults.update(kwargs)
        field = super(MathField, self).formfield(**defaults)
        field.max_length = self.max_length
        return field
