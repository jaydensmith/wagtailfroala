'use strict';

function makeFroalaRichTextEditable(id, options) {
    var input = $('#' + id);
    input.froalaEditor(options);
}

$.FroalaEditor.DEFAULTS.toolbarButtons = ['bold', 'italic', 'underline', 'strikeThrough', 'subscript', 'superscript', 'fontFamily', 'fontSize', '|', 'color', 'paragraphStyle', '|', 'paragraphFormat', 'align', 'formatOL', 'formatUL', 'outdent', 'indent', 'quote', 'insertHR', '-', 'insertLink', 'insertImage', 'insertVideo', 'insertTable', 'undo', 'redo', 'clearFormatting', 'selectAll', 'html'];
$.FroalaEditor.DEFAULTS.imageEditButtons = ['imageAlign', 'imageRemove', '|', 'imageLink', 'linkOpen', 'linkEdit', 'linkRemove', '-', 'imageDisplay', 'imageStyle', 'imageAlt', 'imageSize'];
$.FroalaEditor.DEFAULTS.quickInsertButtons = ['table', 'ul', 'ol', 'hr'];
$.FroalaEditor.DEFAULTS.imagePaste = false;
$.FroalaEditor.DEFAULTS.scrollableContainer = '.content-wrapper';

(function (factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD. Register as an anonymous module.
        define(['jquery'], factory);
    } else if (typeof module === 'object' && module.exports) {
        // Node/CommonJS
        module.exports = function( root, jQuery ) {
            if ( jQuery === undefined ) {
                // require('jQuery') returns a factory that requires window to
                // build a jQuery instance, we normalize how we use modules
                // that require this pattern but the window provided is a noop
                // if it's defined (how jquery works)
                if ( typeof window !== 'undefined' ) {
                    jQuery = require('jquery');
                }
                else {
                    jQuery = require('jquery')(root);
                }
            }
            factory(jQuery);
            return jQuery;
        };
    } else {
        // Browser globals
        factory(jQuery);
    }
}(function ($) {

    'use strict';

    function _loadedCallback (editor, $img) {
        $img.removeClass('fr-uploading');

        // Select the image.
        if ($img.next().is('br')) {
            $img.next().remove();
        }

        editor.image.edit($img);
        editor.events.trigger('image.loaded', [$img]);
    }

    $.FE.RegisterCommand('insertImage', {
        title: 'Insert Image',
        undo: false,
        focus: true,
        refreshAfterCallback: false,
        popup: true,
        callback: function () {
            var editor = this;

            return ModalWorkflow({
                url: window.chooserUrls.imageChooser + '?select_format=true',
                responses: {
                    imageChosen: function(imageData) {
                        editor.edit.off();

                        var $img = $(imageData.html);
                        $img.on('load', function() {
                            _loadedCallback(editor, $(this));
                        });

                        // Make sure we have focus.
                        // Call the event.
                        editor.edit.on();
                        editor.events.focus(true);
                        editor.selection.restore();

                        editor.undo.saveStep();

                        // Insert marker and then replace it with the image.
                        if (editor.opts.imageSplitHTML) {
                            editor.markers.split();
                        } else {
                            editor.markers.insert();
                        }

                        var $marker = editor.$el.find('.fr-marker');
                        $marker.replaceWith($img);

                        editor.html.wrap();
                        editor.selection.clear();

                        editor.events.trigger('contentChanged');
                        editor.undo.saveStep();
                        editor.events.trigger('image.inserted', [$img]);
                    }
                }
            });
        },
        plugin: 'image'
    });
}));
