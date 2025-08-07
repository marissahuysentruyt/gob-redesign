<template>
  <div class="dropdown-demo">
    <div class="container">
      <h1>Dropdown Menu Component Demo</h1>
      <p>Based on SEMrush Core Components Library Design</p>

      <div class="demo-section">
        <h2>Basic Dropdown</h2>
        <div class="demo-grid">
          <div class="demo-item">
            <h3>Small Size</h3>
            <AtomsDropdownMenu
              v-model="selectedValue1"
              :options="basicOptions"
              placeholder="Select an option"
              size="small"
              @change="handleChange"
            />
            <p class="demo-result">Selected: {{ selectedValue1 || "None" }}</p>
          </div>

          <div class="demo-item">
            <h3>Large Size</h3>
            <AtomsDropdownMenu
              v-model="selectedValue2"
              :options="basicOptions"
              placeholder="Select an option"
              size="large"
              @change="handleChange"
            />
            <p class="demo-result">Selected: {{ selectedValue2 || "None" }}</p>
          </div>
        </div>
      </div>

      <div class="demo-section">
        <h2>States</h2>
        <div class="demo-grid">
          <div class="demo-item">
            <h3>Loading State</h3>
            <AtomsDropdownMenu
              :options="[]"
              placeholder="Loading options..."
              size="small"
              :loading="true"
            />
          </div>

          <div class="demo-item">
            <h3>Error State</h3>
            <AtomsDropdownMenu
              :options="[]"
              placeholder="Select an option"
              size="small"
              :error="true"
            />
          </div>

          <div class="demo-item">
            <h3>Empty State</h3>
            <AtomsDropdownMenu
              :options="[]"
              placeholder="Select an option"
              size="small"
            />
          </div>

          <div class="demo-item">
            <h3>Disabled State</h3>
            <AtomsDropdownMenu
              v-model="selectedValue3"
              :options="basicOptions"
              placeholder="Select an option"
              size="small"
              :disabled="true"
            />
          </div>
        </div>
      </div>

      <div class="demo-section">
        <h2>With Disabled Options</h2>
        <div class="demo-item">
          <AtomsDropdownMenu
            v-model="selectedValue4"
            :options="optionsWithDisabled"
            placeholder="Select an option"
            size="large"
            @change="handleChange"
          />
          <p class="demo-result">Selected: {{ selectedValue4 || "None" }}</p>
        </div>
      </div>

      <div class="demo-section">
        <h2>Custom Options</h2>
        <div class="demo-item">
          <AtomsDropdownMenu
            v-model="selectedValue5"
            :options="customOptions"
            placeholder="Choose your favorite color"
            size="large"
            aria-label="Color selection dropdown"
            @change="handleChange"
          />
          <p class="demo-result">Selected: {{ selectedValue5 || "None" }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// No need to import - Nuxt auto-imports components
// import DropdownMenu from "~/components/atoms/dropdown-menu.vue";

interface DropdownOption {
  label: string;
  value: string | number;
  disabled?: boolean;
}

// Reactive data
const selectedValue1 = ref<string | number>("");
const selectedValue2 = ref<string | number>("");
const selectedValue3 = ref<string | number>("option1");
const selectedValue4 = ref<string | number>("");
const selectedValue5 = ref<string | number>("");

// Sample options
const basicOptions: DropdownOption[] = [
  { label: "Option 1", value: "option1" },
  { label: "Option 2", value: "option2" },
  { label: "Option 3", value: "option3" },
  { label: "Option 4", value: "option4" },
  { label: "Option 5", value: "option5" },
  { label: "Option 6", value: "option6" },
  { label: "Option 7", value: "option7" },
  { label: "Option 8", value: "option8" },
  { label: "Option 9", value: "option9" },
  { label: "Option 10", value: "option10" },
];

const optionsWithDisabled: DropdownOption[] = [
  { label: "Available Option 1", value: "available1" },
  { label: "Available Option 2", value: "available2" },
  { label: "Disabled Option 1", value: "disabled1", disabled: true },
  { label: "Available Option 3", value: "available3" },
  { label: "Disabled Option 2", value: "disabled2", disabled: true },
  { label: "Available Option 4", value: "available4" },
];

const customOptions: DropdownOption[] = [
  { label: "Red", value: "red" },
  { label: "Blue", value: "blue" },
  { label: "Green", value: "green" },
  { label: "Yellow", value: "yellow" },
  { label: "Purple", value: "purple" },
  { label: "Orange", value: "orange" },
  { label: "Pink", value: "pink" },
  { label: "Brown", value: "brown" },
];

// Event handlers
const handleChange = (option: DropdownOption) => {
  console.log("Selected option:", option);
};
</script>

<style scoped>
.dropdown-demo {
  min-height: 100vh;
  background-color: #f8f9fa;
  padding: 2rem 0;

  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
  }

  h1 {
    font-size: 2.5rem;
    font-weight: 700;
    color: #191b23;
    margin-bottom: 0.5rem;
    text-align: center;
  }

  p {
    font-size: 1.1rem;
    color: #6c6e79;
    text-align: center;
    margin-bottom: 3rem;
  }

  .demo-section {
    background: white;
    border-radius: 8px;
    padding: 2rem;
    margin-bottom: 2rem;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);

    h2 {
      font-size: 1.5rem;
      font-weight: 600;
      color: #191b23;
      margin-bottom: 1.5rem;
      border-bottom: 2px solid #e0e1e9;
      padding-bottom: 0.5rem;
    }
  }

  .demo-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
  }

  .demo-item {
    h3 {
      font-size: 1.1rem;
      font-weight: 500;
      color: #191b23;
      margin-bottom: 1rem;
    }

    .demo-result {
      margin-top: 0.5rem;
      font-size: 0.9rem;
      color: #6c6e79;
      font-style: italic;
    }
  }
}

/* Responsive design */
@media (max-width: 768px) {
  .dropdown-demo {
    padding: 1rem 0;

    .container {
      padding: 0 0.5rem;
    }

    h1 {
      font-size: 2rem;
    }

    .demo-section {
      padding: 1.5rem;
    }

    .demo-grid {
      grid-template-columns: 1fr;
      gap: 1.5rem;
    }
  }
}
</style>
