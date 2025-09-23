// Reusable component prop types
export interface ButtonProps {
  variant?: "success" | "primary" | "secondary" | "danger" | "warning";
  size?: "small" | "large";
  disabled?: boolean;
  loading?: boolean;
  type?: "button" | "submit" | "reset";
}
export interface HeadingProps {
  level?: "1" | "2" | "3" | "4" | "5" | "6"; // for dynamic tag rendering
  title?: string;
  url?: string;
}

export interface LinkProps {
  url: string;
  title?: string;
  isActive?: boolean;
}
