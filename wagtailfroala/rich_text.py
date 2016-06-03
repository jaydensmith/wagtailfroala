from __future__ import absolute_import, unicode_literals

import json

from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.forms import Media, widgets
from django.utils.module_loading import import_string

from wagtail.utils.widgets import WidgetWithScript
from wagtail.wagtailadmin.edit_handlers import RichTextFieldPanel
from wagtail.wagtailcore.rich_text import DbWhitelister, expand_db_html


class FroalaRichTextArea(WidgetWithScript, widgets.Textarea):
    def get_panel(self):
        return RichTextFieldPanel

    def render(self, name, value, attrs=None):
        if value is None:
            translated_value = None
        else:
            translated_value = expand_db_html(value, for_editor=True)
        return super(FroalaRichTextArea, self).render(name, translated_value, attrs)

    def render_js_init(self, id_, name, value):
        froala_options = getattr(settings, 'FROALA_OPTIONS', {})
        froala_options.update({
            'key': settings.FROALA_LICENSE_KEY,
            'scrollableContainer': '.content-wrapper'
        })
        
        return "makeFroalaRichTextEditable({0}, {1});".format(
            json.dumps(id_),
            json.dumps(froala_options)
        )

    def value_from_datadict(self, data, files, name):
        original_value = super(FroalaRichTextArea, self).value_from_datadict(data, files, name)
        if original_value is None:
            return None
        return DbWhitelister.clean(original_value)

    @property
    def media(self):
        return Media(js=[
            static('froala/vendor/js/froala_editor.pkgd.min.js'),
            '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.3.0/codemirror.min.js',
            '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.3.0/mode/xml/xml.min.js',
            static('froala/js/froala.js'),

        ], css={
            'all': [
                static('froala/vendor/css/froala_editor.pkgd.min.css'),
                '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.3.0/codemirror.min.css',
                '//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css',
            ]
        })
