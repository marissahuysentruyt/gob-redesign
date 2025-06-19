// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2025-05-15",
  devtools: { enabled: true },

  modules: ["@nuxt/image", "@nuxt/content", "@nuxt/eslint", "@nuxt/test-utils"],

  // Runtime configuration for environment variables
  runtimeConfig: {
    // Private keys (only available on server-side)
    supabaseUrl: process.env.SUPABASE_URL,
    supabaseKey: process.env.SUPABASE_KEY,

    // Public keys (exposed to client-side)
    public: {
      supabaseUrl: process.env.SUPABASE_URL,
      // Note: Only use anon/public keys in public config
      supabaseAnonKey: process.env.SUPABASE_KEY,
    },
  },
});
