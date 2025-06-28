<script setup lang="ts">
import type { LinkProps } from "~/types/index";

const props = withDefaults(defineProps<LinkProps>(), {
  url: "/", // defaults to homepage if no url is provided
  isActive: false,
});

// Add the missing isActive logic
const route = useRoute();
const isActive = computed(() => route.path === props.url);
</script>

<template>
  <NuxtLink
    class="cmp-link"
    :class="{ 'cmp-link--active': isActive }"
    :to="props.url"
  >
    <span class="cmp-link__text">
      <slot />
    </span>
  </NuxtLink>
</template>

<style scoped>
.cmp-link {
  color: red;
}
</style>
