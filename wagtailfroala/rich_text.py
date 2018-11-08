from __future__ import absolute_import, unicode_literals

import functools
import json
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.forms import Media, widgets
from wagtail import __version__ as WAGTAIL_VERSION
from wagtail.utils.widgets import WidgetWithScript

if WAGTAIL_VERSION >= '2.0':
    from wagtail.admin.edit_handlers import RichTextFieldPanel
    from wagtail.admin.rich_text.converters.editor_html import DbWhitelister
    from wagtail.core.rich_text import expand_db_html

    db_white_lister = DbWhitelister(DbWhitelister.element_rules)
else:
    from wagtail.wagtailadmin.edit_handlers import RichTextFieldPanel
    from wagtail.wagtailcore.rich_text import DbWhitelister, expand_db_html

    expand_db_html = functools.partial(expand_db_html, for_editor=True)
    db_white_lister = DbWhitelister


class FroalaRichTextArea(WidgetWithScript, widgets.Textarea):
    def __init__(self, **kwargs):
        try:
            self.options = kwargs.pop('options')
        except KeyError:
            self.options = {
                'key': settings.FROALA_LICENSE_KEY
            }
            self.options.update(getattr(settings, 'FROALA_OPTIONS', {}))

        super(FroalaRichTextArea, self).__init__(**kwargs)

    def get_panel(self):
        return RichTextFieldPanel

    def render(self, name, value, attrs=None, **kwargs):
        if value is None:
            translated_value = None
        else:
            translated_value = expand_db_html(value)
        return super(FroalaRichTextArea, self).render(name, translated_value, attrs, **kwargs)

    def render_js_init(self, id_, name, value):
        return "makeFroalaRichTextEditable({0}, {1});".format(
            json.dumps(id_),
            json.dumps(self.options)
        )

    def value_from_datadict(self, data, files, name):
        original_value = super(FroalaRichTextArea, self).value_from_datadict(data, files, name)
        if original_value is None:
            return None
        return db_white_lister.clean(original_value)

    @property
    def media(self):
        js = [
            static('froala/vendor/js/froala_editor.pkgd.min.js'),
        ]

        css = [
            static('froala/css/wagtailfroala.css'),
            static('froala/vendor/css/froala_editor.pkgd.min.css'),
            '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.3.0/codemirror.min.css',
            '//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css',
        ]

        if getattr(settings, 'FROALA_CODEMIRROR', True):
            js.append('//cdnjs.cloudflare.com/ajax/libs/codemirror/5.3.0/codemirror.min.js')
            js.append('//cdnjs.cloudflare.com/ajax/libs/codemirror/5.3.0/mode/xml/xml.min.js')
            css.append('//cdnjs.cloudflare.com/ajax/libs/codemirror/5.3.0/codemirror.min.css')

        # Maintain the order of JavaScript files.
        js.append(static('froala/js/froala.js'))

        if getattr(settings, 'FROALA_FONT_AWESOME', True):
            css.append('//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css')

        return Media(js=js, css={
            'all': css
        })
