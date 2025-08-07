<template>
  <div
    class="dropdown-menu"
    :class="[`dropdown-menu--${size}`, { 'dropdown-menu--open': isOpen }]"
  >
    <!-- Trigger Button -->
    <button
      ref="triggerRef"
      type="button"
      class="dropdown-menu__trigger"
      :class="[`dropdown-menu__trigger--${size}`]"
      @click="toggleDropdown"
      @keydown.escape="closeDropdown"
      @keydown.enter="toggleDropdown"
      @keydown.space.prevent="toggleDropdown"
      :aria-expanded="isOpen"
      :aria-haspopup="true"
      :disabled="disabled"
    >
      <span class="dropdown-menu__trigger-text">{{
        selectedOption || placeholder
      }}</span>
      <svg
        class="dropdown-menu__trigger-icon"
        :class="{ 'dropdown-menu__trigger-icon--rotated': isOpen }"
        width="16"
        height="16"
        viewBox="0 0 16 16"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M4 6L8 10L12 6"
          stroke="currentColor"
          stroke-width="1.5"
          stroke-linecap="round"
          stroke-linejoin="round"
        />
      </svg>
    </button>

    <!-- Dropdown Menu -->
    <Transition name="dropdown">
      <div
        v-if="isOpen"
        ref="menuRef"
        class="dropdown-menu__menu"
        :class="[`dropdown-menu__menu--${size}`]"
        role="listbox"
        :aria-label="ariaLabel"
      >
        <!-- Loading State -->
        <div
          v-if="loading"
          class="dropdown-menu__item dropdown-menu__item--loading"
          :class="[`dropdown-menu__item--${size}`]"
        >
          <span class="dropdown-menu__item-text">Loading...</span>
        </div>

        <!-- Error State -->
        <div
          v-else-if="error"
          class="dropdown-menu__item dropdown-menu__item--error"
          :class="[`dropdown-menu__item--${size}`]"
        >
          <span class="dropdown-menu__item-text"
            >Something went wrong. Please try again later.</span
          >
        </div>

        <!-- Empty State -->
        <div
          v-else-if="!options || options.length === 0"
          class="dropdown-menu__item dropdown-menu__item--empty"
          :class="[`dropdown-menu__item--${size}`]"
        >
          <span class="dropdown-menu__item-text">Nothing found</span>
        </div>

        <!-- Options List -->
        <template v-else>
          <div
            v-for="(option, index) in options"
            :key="option.value || index"
            class="dropdown-menu__item"
            :class="[
              `dropdown-menu__item--${size}`,
              {
                'dropdown-menu__item--selected': option.value === selectedValue,
                'dropdown-menu__item--disabled': option.disabled,
              },
            ]"
            role="option"
            :aria-selected="option.value === selectedValue"
            @click="selectOption(option)"
            @keydown.enter="selectOption(option)"
            @keydown.space.prevent="selectOption(option)"
            tabindex="0"
          >
            <span class="dropdown-menu__item-text">{{ option.label }}</span>
            <svg
              v-if="option.value === selectedValue"
              class="dropdown-menu__item-check"
              width="16"
              height="16"
              viewBox="0 0 16 16"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M13 4L6 11L3 8"
                stroke="currentColor"
                stroke-width="1.5"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
          </div>
        </template>
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
interface DropdownOption {
  label: string;
  value: string | number;
  disabled?: boolean;
}

interface Props {
  options?: DropdownOption[];
  modelValue?: string | number;
  placeholder?: string;
  size?: "small" | "large";
  disabled?: boolean;
  loading?: boolean;
  error?: boolean;
  ariaLabel?: string;
}

const props = withDefaults(defineProps<Props>(), {
  options: () => [],
  placeholder: "Select an option",
  size: "small",
  disabled: false,
  loading: false,
  error: false,
  ariaLabel: "Dropdown menu",
});

const emit = defineEmits<{
  "update:modelValue": [value: string | number];
  change: [option: DropdownOption];
}>();

const isOpen = ref(false);
const triggerRef = ref<HTMLButtonElement>();
const menuRef = ref<HTMLDivElement>();

const selectedValue = computed(() => props.modelValue);
const selectedOption = computed(() => {
  const option = props.options.find((opt) => opt.value === selectedValue.value);
  return option?.label;
});

const toggleDropdown = () => {
  if (props.disabled) return;
  isOpen.value = !isOpen.value;
};

const closeDropdown = () => {
  isOpen.value = false;
};

const selectOption = (option: DropdownOption) => {
  if (option.disabled) return;

  emit("update:modelValue", option.value);
  emit("change", option);
  closeDropdown();
};

// Close dropdown when clicking outside
onMounted(() => {
  const handleClickOutside = (event: Event) => {
    const target = event.target as HTMLElement;
    const trigger = triggerRef.value;
    const menu = menuRef.value;

    if (
      trigger &&
      menu &&
      !trigger.contains(target) &&
      !menu.contains(target)
    ) {
      closeDropdown();
    }
  };

  document.addEventListener("click", handleClickOutside);

  onUnmounted(() => {
    document.removeEventListener("click", handleClickOutside);
  });
});

// Close dropdown on escape key
onMounted(() => {
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && isOpen.value) {
      closeDropdown();
    }
  });
});
</script>

<style scoped>
.dropdown-menu {
  position: relative;
  display: inline-block;
  width: 100%;
  max-width: 240px;

  &__trigger {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    padding: 6px 8px;
    background: #ffffff;
    border: 1px solid #e0e1e9;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
    font-family: "Inter", sans-serif;
    font-weight: 400;
    color: #191b23;

    &:hover:not(:disabled) {
      border-color: #c0c1c9;
    }

    &:focus {
      outline: none;
      border-color: #007bff;
      box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.25);
    }

    &:disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }

    &--small {
      font-size: 14px;
      line-height: 1.43;
      min-height: 32px;
    }

    &--large {
      font-size: 16px;
      line-height: 1.5;
      min-height: 40px;
      padding: 8px 12px;
    }
  }

  &__trigger-text {
    flex: 1;
    text-align: left;
  }

  &__trigger-icon {
    margin-left: 8px;
    transition: transform 0.2s ease;
    color: #6c6e79;

    &--rotated {
      transform: rotate(180deg);
    }
  }

  &__menu {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    z-index: 1000;
    background: #ffffff;
    border: 1px solid #e0e1e9;
    border-radius: 6px;
    box-shadow: 0px 1px 12px 0px rgba(25, 27, 35, 0.15);
    margin-top: 4px;
    overflow: hidden;
    min-width: 100%;

    &--small {
      padding: 4px 0;
    }

    &--large {
      padding: 4px 0;
    }
  }

  &__item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    cursor: pointer;
    transition: background-color 0.2s ease;
    font-family: "Inter", sans-serif;
    font-weight: 400;
    color: #191b23;

    &:hover:not(&--disabled):not(&--loading):not(&--error):not(&--empty) {
      background-color: #f8f9fa;
    }

    &:focus {
      outline: none;
      background-color: #f8f9fa;
    }

    &--small {
      padding: 6px 8px;
      font-size: 14px;
      line-height: 1.43;
    }

    &--large {
      padding: 8px 12px;
      font-size: 16px;
      line-height: 1.5;
    }

    &--selected {
      background-color: #f0f8ff;
      color: #007bff;
    }

    &--disabled {
      opacity: 0.5;
      cursor: not-allowed;
      color: #6c6e79;
    }

    &--loading,
    &--error,
    &--empty {
      cursor: default;
      color: #6c6e79;
      justify-content: center;
    }
  }

  &__item-text {
    flex: 1;
    text-align: left;
  }

  &__item-check {
    margin-left: 8px;
    color: #007bff;
  }
}

/* Transition animations */
.dropdown-enter-active,
.dropdown-leave-active {
  transition: all 0.2s ease;
}

.dropdown-enter-from,
.dropdown-leave-to {
  opacity: 0;
  transform: translateY(-4px);
}

.dropdown-enter-to,
.dropdown-leave-from {
  opacity: 1;
  transform: translateY(0);
}
</style>
