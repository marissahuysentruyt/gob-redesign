<script setup lang="ts">
import type { HeadingProps } from "~/types/index";

const props = withDefaults(defineProps<HeadingProps>(), {
  level: "1", // defaults to h1
  title: "Heading", // defaults to "heading"
});
</script>

<template>
  <component :is="`h${props.level}`">
    {{ props.title }}
  </component>
</template>

<style scoped>
h1 {
  font-size: 2rem;
}
</style>
