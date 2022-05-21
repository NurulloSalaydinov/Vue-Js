<template>
  <div class="element"></div>
</template>

<script>
import { Editor } from '@tiptap/core'
import Document from "@tiptap/extension-document";
import Paragraph from "@tiptap/extension-paragraph";
import Text from "@tiptap/extension-text";

export default {
  mounted() {
    const editor = new Editor({
      element: document.querySelector(".element"),
      extensions: [Document, Paragraph, Text],
      content: "<p>Example Text</p>",
      autofocus: true,
      editable: true,
      injectCSS: false
    });
  }
};
</script>
