from django import forms

import json


class CroppieWidget(forms.FileInput):
    template_name = 'croppie/widget.html'

    def __init__(self, options=None, *args, **kwargs):
        self.croppie_options = options
        super(CroppieWidget, self).__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        context = super(CroppieWidget, self).get_context(name, value, attrs)
        context['widget'].update({
            'croppie_options': json.dumps(self.croppie_options),
        })
        return context

    class Media:
        css = {
            'all': (
                'croppie/croppie.css',
            )
        }
        js = (
            'croppie/croppie.min.js',
            'croppie/form-process.js',
        )


class CroppieImageRatioWidget(forms.MultiWidget):
    def __init__(self, options=None, *args, **kwargs):
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
