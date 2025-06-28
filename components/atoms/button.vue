<template>
  <button class="cmp-button">
    <slot />
  </button>
</template>

<script setup lang="ts"></script>

<style scoped>
.cmp-button {
  --button-text-color: #ffffff;
  --button-background-color: #5925ab;

  color: var(--button-text-color);
  background-color: var(--button-background-color);
  appearance: none;
  border: none;
}
</style>
