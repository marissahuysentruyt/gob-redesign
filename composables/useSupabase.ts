import { createClient } from "@supabase/supabase-js";

export const useSupabase = () => {
  const config = useRuntimeConfig();

  const supabase = createClient(
    config.public.supabaseUrl,
    config.public.supabaseAnonKey,
  );

  return {
    supabase,

    // Helper methods for common operations
    async getInventory(limit = 100) {
      const { data, error } = await supabase
        .from("inventory")
        .select("*")
        .limit(limit);

      if (error) {
        console.error("Error fetching inventory:", error);
        throw error;
      }

      return data;
    },

    async getInventoryItem(id: string) {
      const { data, error } = await supabase
        .from("inventory")
        .select("*")
        .eq("id", id)
        .single();

      if (error) {
        console.error("Error fetching inventory item:", error);
        throw error;
      }

      return data;
    },

    async searchInventory(searchTerm: string) {
      const { data, error } = await supabase
        .from("inventory")
        .select("*")
        .or(
          `name.ilike.%${searchTerm}%,description.ilike.%${searchTerm}%,type.ilike.%${searchTerm}%`,
        );

      if (error) {
        console.error("Error searching inventory:", error);
        throw error;
      }

      return data;
    },

    async insertInventoryItem(item: any) {
      const { data, error } = await supabase
        .from("inventory")
        .insert(item)
        .select();

      if (error) {
        console.error("Error inserting inventory item:", error);
        throw error;
      }

      return data;
    },

    async updateInventoryItem(id: string, updates: any) {
      const { data, error } = await supabase
        .from("inventory")
        .update(updates)
        .eq("id", id)
        .select();

      if (error) {
        console.error("Error updating inventory item:", error);
        throw error;
      }

      return data;
    },

    async deleteInventoryItem(id: string) {
      const { data, error } = await supabase
        .from("inventory")
        .delete()
        .eq("id", id);

      if (error) {
        console.error("Error deleting inventory item:", error);
        throw error;
      }

      return data;
    },
  };
};
