import io
import base64
import logging

from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile

from PIL import Image

from croppie.widgets import CroppieImageRatioWidget


class CroppieField(forms.MultiValueField):

    def __init__(self, options={}, widget=None, *args, **kwargs):
        fields = (
            forms.ImageField(),
            forms.CharField()
        )
        if widget is None:
            widget = CroppieImageRatioWidget(options=options)

        super(CroppieField, self).__init__(
            fields=fields, widget=widget, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            data_base64 = data_list[1]
            return self.unpack_image(data_base64)

    def unpack_image(self, base64_payload):
        """Convert base64 data to an image file"""
        image_format, base64_data = base64_payload.split(',', 1)
        content_type, payload_format = image_format.split(';')
        content_type = content_type.split(':', 1)[1]
        if payload_format != 'base64':
            raise ValueError("Image is not base64 encoded")
        image_blob = io.BytesIO(base64.b64decode(bytes(base64_data, 'utf-8')))

        return InMemoryUploadedFile(
            image_blob,
            'avatar',
            'uploaded_file.png'
            'image/png',
            None,
            None,
            None,
        )
