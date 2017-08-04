from django import forms

import json


class BaseCroppieWidget(forms.FileInput):
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

    def __init__(self, options, *args, **kwargs):
        self.croppie_options = options
        super(BaseCroppieWidget, self).__init__(*args, **kwargs)

    def process_croppie_context(self, name):
        name = name.replace('_0', '')
        return {
            'croppie_options': json.dumps(self.croppie_options),
            'croppie_field_name': name,
        }
