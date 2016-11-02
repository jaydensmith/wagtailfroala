===============
Wagtail Froala
===============

Extends Wagtail to use the amazing Froala editor.
This Wagtail extension requires Wagtail 1.5.x, as it uses ``WAGTAILADMIN_RICH_TEXT_EDITORS``.

Installation
============

Run the command ``pip install wagtailfroala``

Add ``wagtailfroala`` to your ``INSTALLED_APPS``.

Add ``wagtailfroala.rich_text.FroalaRichTextArea`` to ``WAGTAILADMIN_RICH_TEXT_EDITORS`` in your settings.

For example, to use Froala for all ``RichTextField`` and ``RichTextBlock`` instances:

.. code-block:: python

    WAGTAILADMIN_RICH_TEXT_EDITORS = {
        'default': {
            'WIDGET': 'wagtailfroala.rich_text.FroalaRichTextArea',
            'OPTIONS': {
                'key': 'xxxxxxxxxxxx'
             }
        }
    }

Or, to use Froala only for defined instances...

.. code-block:: python
    
    WAGTAILADMIN_RICH_TEXT_EDITORS = {
        'default': {
            'WIDGET': 'wagtail.wagtailadmin.rich_text.HalloRichTextArea'
        },
        'froala': {
            'WIDGET': 'wagtailfroala.rich_text.FroalaRichTextArea',
            'OPTIONS': {
                'key': 'xxxxxxxxxxxx',
                'toolbarButtons': [
                    'paragraphFormat', 'fontFamily', 'bold', 'italic',
                    'underline', 'formatOL', 'formatUL', 'align',
                    'color', '|', 'insertHR', 'insertLink', '|', 'undo', 'redo'
                ]
            }
        },
        'froala_small': {
            'WIDGET': 'wagtailfroala.rich_text.FroalaRichTextArea',
            'OPTIONS': {
                'key': 'xxxxxxxxxxxx',
                'toolbarButtons': ['fontFamily', 'bold', 'italic', 'underline', 'color', '|', 'insertLink'],
                'editorClass': 'editor-small'
            }
        }
    }

.. code-block:: python

    html_field = RichTextField(editor='froala')
    stream_field = StreamField([
        ('html', RichTextBlock(editor='froala_small'))
    ])

Options
-------

You will need to ensure that the ``key`` option is correctly set with your Froala license key.

By default, Codemirror HTML syntax highlighting is enabled, you can disable it if you wish.

.. code-block:: python
    
    FROALA_CODEMIRROR = False

Font Awesome is required by Froala for toolbar icons, so it is included by default. If you don't want to include it or already have a version included, you can disable it.

.. code-block:: python
    
    FROALA_FONT_AWESOME = False

To Do
-------
- [ ] Implement image replace button.
- [ ] Incoorperate Froala events https://www.froala.com/wysiwyg-editor/docs/events.


Please feel free to contribute.