===============
Wagtail Froala
===============

Extends Wagtail to use the amazing Froala editor.
This Wagtail extension requires Wagtail 1.5.x, as it uses ``WAGTAILADMIN_RICH_TEXT_EDITORS``.

Installation
============

Run the command
``pip install wagtailfroala``

Add ``wagtailfroala`` to your ``INSTALLED_APPS``.

Add ``wagtailfroala.rich_text.FroalaRichTextArea`` to ``WAGTAILADMIN_RICH_TEXT_EDITORS`` in your settings.

For example, to use Froala for all ``RichTextField`` and ``RichTextBlock`` instances:

.. code-block:: python

    WAGTAILADMIN_RICH_TEXT_EDITORS = {
        'default': {
            'WIDGET': 'wagtailfroala.rich_text.FroalaRichTextArea'
        },
    }

Or, to use Froala only for defined instances...

.. code-block:: python
    
    WAGTAILADMIN_RICH_TEXT_EDITORS = {
        'default': {
            'WIDGET': 'wagtail.wagtailadmin.rich_text.HalloRichTextArea'
        },
        'froala': {
            'WIDGET': 'wagtailfroala.rich_text.FroalaRichTextArea'
        },
    }

.. code-block:: python

    html_field = RichTextField(editor='froala')
    stream_field = StreamField([
        ('html', RichTextBlock(editor='froala'))
    ])

Options
-------

You will need to add ``FROALA_LICENSE_KEY`` to your settings:

.. code-block:: python

    FROALA_LICENSE_KEY = 'xxxxxxxxxxxxxx';

You can also specify ``FROALA_OPTIONS``, which should be a dict populated with official Froala options (https://www.froala.com/wysiwyg-editor/docs/options):

.. code-block:: python

    FROALA_OPTIONS = {
        'toolbarButtonsMD': ['bold', 'italic', 'underline', 'fontFamily', 'fontSize', 'color'],
        'toolbarButtonsXS': ['bold', 'italic', 'underline']
    };

To Do
-------
- [ ] Incoorperate page chooser for links (like hallo.js).
- [ ] Incoorperate document chooser for links (like hallo.js).
- [ ] Incoorperate image chooser (like hallo.js).
