<script setup lang="ts">
import type { ButtonProps } from "~/types/index";

const props = withDefaults(defineProps<ButtonProps>(), {
  variant: "success",
  size: "small",
  disabled: false,
  loading: false,
  type: "button",
});
</script>

<template>
  <button
    class="cmp-button"
    :class="[`cmp-button--${props.variant}`, `cmp-button--${props.size}`, { 'is-loading': props.loading }]"
    :disabled="props.disabled || props.loading"
    :type="props.type"
    :aria-busy="props.loading || undefined"
  >
    <span class="cmp-button__label"><slot /></span>
  </button>
  
</template>

<style scoped>
.cmp-button {
  /* Base layout */
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  border-radius: 6px;
  border: 1px solid transparent;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
  text-decoration: none;
  transition: background-color 0.15s ease, color 0.15s ease, border-color 0.15s ease, box-shadow 0.15s ease, opacity 0.15s ease;
  font-family: "Inter", system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
  font-weight: 600;

  /* Theming via CSS variables set by variants */
  color: var(--button-text, #ffffff);
  background-color: var(--button-bg, #22c55e);
  border-color: var(--button-border, transparent);
}

.cmp-button:is(:hover, :focus-visible):not(:disabled) {
  background-color: var(--button-bg-hover, #16a34a);
}

.cmp-button:active:not(:disabled) {
  background-color: var(--button-bg-active, #15803d);
}

.cmp-button:focus-visible {
  outline: none;
  box-shadow: var(--button-focus-ring, 0 0 0 3px rgba(34, 197, 94, 0.3));
}

.cmp-button:disabled,
.cmp-button.is-loading {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Sizes */
.cmp-button--small {
  padding: 8px 12px;
  font-size: 14px;
  line-height: 1.43;
}

.cmp-button--large {
  padding: 10px 16px;
  font-size: 16px;
  line-height: 1.5;
}

.cmp-button__label {
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

/* Variant: success (default) */
.cmp-button--success {
  --button-text: #ffffff;
  --button-bg: #22c55e; /* base */
  --button-bg-hover: #16a34a; /* hover/focus */
  --button-bg-active: #15803d; /* active */
  --button-border: transparent;
  --button-focus-ring: 0 0 0 3px rgba(34, 197, 94, 0.3);
}
</style>
