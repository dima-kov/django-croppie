from .base import BaseCroppieWidget


class CroppieWidget(BaseCroppieWidget):
    """
        Widget for Django.VERSION >= 11
    """

    template_name = 'croppie/widget.html'

    def get_context(self, name, value, attrs):
        context = super(CroppieWidget, self).get_context(name, value, attrs)
        name = context['widget'].get('name')
        context['widget'].update(
            self.process_croppie_context(name)
        )
        return context
