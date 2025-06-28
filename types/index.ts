// Reusable component prop types
// TODO: add button props to component
// export interface ButtonProps {
//   variant?: 'primary' | 'secondary' |
//   size?: 'sm' | 'md' | 'lg'
//   disabled?: boolean
//   loading?: boolean
// }
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
