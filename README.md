# Django Croppie

Django-croppie is an application for easy integration [croppie.js](https://github.com/Foliotek/Croppie) image cropper to django projects.

# Installation

1. Install with `pip install django-croppie`

2. Add `croppie` to `INSTALLED_APPS`:

```
INSTALLED_APPS = [
    ...
    'croppie',
    ...
]
```

# Usage

1. To use django-croppie you should specify a form field:

```
from croppie.fields import CroppieField

class AddForm(forms.Form):
    photo = CroppieField()
```

Also `CroppieField` takes non required argument `options` - a python dictionary that represent `croppie.js` settings. For example:

```
    photo = CroppieField(
        options={
            'viewport': {
                'width': 120,
                'height': 140,
            },
            'boundary': {
                'width': 200,
                'height': 220,
            },
            'showZoomer': True,
        },
    )
```
2. Add form static files to template:

```
{% block js %}
    {{ form.media }}
{% endblock js %}
```

3. Specify position of cropper widget on page:

```
    <div class="row">
        <div id="cropper"></div>
    </div>
```

4. That's all!

# Example

There is an example project in the `example` directory. Read `README.md` for deploy instructions.
