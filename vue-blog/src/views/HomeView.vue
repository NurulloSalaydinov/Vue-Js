<!-- <template>
  <div id="app">
    <div id="codex-editor"></div>
  </div>
</template>

<script>
import EditorJS from "@editorjs/editorjs";
import Headers from "@editorjs/header";
import List from "@editorjs/list";
import Code from '@editorjs/code'
import Paragraph from '@editorjs/paragraph'
import Embed from '@editorjs/embed'
import Table from '@editorjs/table'
import Checklist from '@editorjs/checklist'
import Marker from '@editorjs/marker'
import Warning from '@editorjs/warning'
import RawTool from '@editorjs/raw'
import Quote from '@editorjs/quote'
import InlineCode from '@editorjs/inline-code'
import Delimiter from '@editorjs/delimiter'
import Image from '@editorjs/image'

  // EditorJS = require('@editorjs/editorjs')
  // Image = require('@editorjs/image')
// Headers = require('@editorjs/header')
// Embed = require('@editorjs/embed')
// List = require('@editorjs/list')
// Code = require('@editorjs/code')
// Quote = require('@editorjs/quote')

export default {
  name: "Home",
  mounted() {
    const editor = new EditorJS({
      onReady: () => {
        // eslint-disable-next-line no-new
      },
      holder: 'codex-editor',
      tools: {
        embed: Embed,
        
        list: {
          class: List,
          inlineToolbar: true,
        },
        quote: {
          class: Quote,
          inlineToolbar: true,
          config: {
            quotePlaceholder: 'Iqtibos kiriting',
            captionPlaceholder: 'Iqtibos muallifini kiriting',
          },
        },
        header: {
          class: Headers,
          levels: [2, 3, 4],
          defaultLevel: 3,
          inlineToolbar: true,
          placeholder: 'Enter a header',
        },
        marker: {
          class: Marker
        },
        Table,
        image: {
      class: Image,
      config: {
        endpoints: {
          byFile: 'http://127.0.0.1:8000/upload/', // Your backend file uploader endpoint
          byUrl: 'http://localhost/upload/', // Your endpoint that provides uploading by Url
        }
      }
    }
      },
      placeholder:
        'Toolni tanlash uchun ‘+’ ni bosing.',
      i18n: {
        /**
         * @type {I18nDictionary}
         */
        messages: {
          /**
           * Other below: translation of different UI components of the editor.js core
           */
          ui: {
            blockTunes: {
              toggler: {
                'Click to tune': 'Sozlash uchun bosing',
                'or drag to move': 'O’rin almashtirish uchun sudrang',
              },
            },
            inlineToolbar: {
              converter: {
                'Convert to': 'O‘zgartirish',
              },
            },
            toolbar: {
              toolbox: {
                Add: 'Pastda blok qo’shish uchun bosing',
              },
            },
          },

          /**
           * Section for translation Tool Names: both block and inline tools
           */
          toolNames: {
            Text: 'Paragraf',
            Heading: 'Sarlavha',
            List: 'Ro’yhat',
            Warning: 'Примечание',
            Checklist: 'Чеклист',
            Quote: 'Iqtibos',
            Code: 'Kod',
            Image: 'Rasm',
            Delimiter: 'Разделитель',
            'Raw HTML': 'HTML-фрагмент',
            Table: 'Таблица',
            Link: 'Havola',
            Marker: 'Маркер',
            Bold: 'Qalin',
            Italic: 'Kursiv',
            InlineCode: 'Моноширинный',
          },

          /**
           * Section for passing translations to the external tools classes
           */
          tools: {
            /**
             * Each subsection is the i18n dictionary that will be passed to the corresponded plugin
             * The name of a plugin should be equal the name you specify in the 'tool' section for that plugin
             */
            warning: {
              // <-- 'Warning' tool will accept this dictionary section
              Title: 'Название',
              Message: 'Сообщение',
            },
            list: {
              // <-- 'List' tool will accept this dictionary section
              Unordered: 'Belgili ro‘yxat',
              Ordered: 'Raqamlangan ro’yhat',
            },
            image: {
              // <-- 'Image' tool will accept this dictionary section
              Insert: 'Вставить',
              Upload: 'Загрузить',
              ByURL: 'По URL',
              Browse: 'Обзор',
              Caption: ' ',
              // translate 'Select an image' to 'Select a picture'
              // what is the kay of it ?
              'Select an Image': 'Rasm tanlang',
              'Stretch image': 'Rasmni cho’zish',
              'With border': 'Chegara bilan',
              'With background': 'Fonida',
            },
            code: {
              'Enter a code': 'Kod kiriting',
            },

            /**
             * Link is the internal Inline Tool
             */
            link: {
              'Add a link': 'Havola qo‘shing',
            },
            /**
             * The "stub" is an internal block tool, used to fit blocks that does not have the corresponded plugin
             */
            stub: {
              'The block can not be displayed correctly.':
                'Блок не может быть отображен',
            },
          },

          /**
           * Section allows to translate Block Tunes
           */
          blockTunes: {
            /**
             * Each subsection is the i18n dictionary that will be passed to the corresponded Block Tune plugin
             * The name of a plugin should be equal the name you specify in the 'tunes' section for that plugin
             *
             * Also, there are few internal block tunes: "delete", "moveUp" and "moveDown"
             */
            delete: {
              Delete: 'O‘chirish',
            },
            moveUp: {
              'Move up': 'Tepaga kochirish',
            },
            moveDown: {
              'Move down': 'Pastga kochirish',
            },
          },
        },
      },
    })
  },
}
</script> -->
