import django
from django import forms

if django.VERSION[0] <= 1 and django.VERSION[1] < 11:
    from .widgets_old import CroppieWidget
else:
    from .widgets import CroppieWidget


class CroppieImageRatioWidget(forms.MultiWidget):
    def __init__(self, options, *args, **kwargs):
        widgets = (
            CroppieWidget(options=options),
            forms.HiddenInput(),
            forms.HiddenInput(),
            forms.HiddenInput(),
            forms.HiddenInput(),
        )
        super(CroppieImageRatioWidget, self).__init__(
            widgets=widgets,
            *args, **kwargs
        )

    def decompress(self, value):
        if value:
            return [value, None, None, None, None]
        return [None, None, None, None, None]
