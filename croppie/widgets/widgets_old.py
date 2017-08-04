from django.utils.html import format_html, mark_safe

from .base import BaseCroppieWidget


class CroppieWidget(BaseCroppieWidget):
    """
        Widget for Django.VERSION < 11 as old versions
        of django does not support templates in widgets.
    """

    def render(self, name, value, attrs=None):
        html = super(CroppieWidget, self).render(name, value, attrs)
        html += format_html(
            '<script type="text/javascript">{}</script>',
            self.make_script_vars(name),
        )
        return html

    def make_script_vars(self, name):
        context = self.process_croppie_context(name)
        vars = 'var croppieFieldName = "{}"\n var croppieOptions = {}' \
            .format(
                context['croppie_field_name'],
                context['croppie_options'],
            )
        return mark_safe(vars)
