from django import forms


class CroppieWidget(forms.FileInput):
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
    def __init__(self, *args, **kwargs):
        widgets = (
            CroppieWidget(),
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
