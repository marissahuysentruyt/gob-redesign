# GOB Redesign Project

This side project redesigns the GOB website with modern features and improved user experience. Built with Nuxt.js and the Semrush Intergalactic design system.

## Features

- Responsive design for all devices
- Improved navigation and search functionality
- Enhanced accessibility and usability
- Modern design patterns and components
- User-friendly interface
- E-commerce functionality

## Tech stack

- Bun
- Nuxt.js
- TypeScript
- Supabase
- Python

## Quick Nuxt Starter

Look at the [Nuxt documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.
### 1. Clone and Install Dependencies

```bash
git clone <repository-url>
cd gob-redesign
bun install
```

### 2. Environment Setup

Copy the environment template:
```bash
cp .env.example .env
```

Edit `.env` with your actual credentials:
```env
# Supabase Configuration
SUPABASE_URL=https://your-project-ref.supabase.co
SUPABASE_KEY=your-anon-key-here

# Application Configuration
NODE_ENV=development
```

### 3. Python Setup (for data scraping)

```bash
cd python
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
deactivate  # To exit virtual environment
```

### 4. Development Server

```bash
bun run dev
```

Visit `http://localhost:3000` to see your application.

## Available Scripts

### Frontend Development
```bash
bun run dev          # Start development server
bun run build        # Build for production
bun run generate     # Generate static site
bun run preview      # Preview production build
```

### Data Management
```bash
# Activate Python environment and run scraper
cd python
source venv/bin/activate
python main.py       # Scrape and populate database
deactivate
```

## Project Structure

```
gob-redesign/
├── app.vue                    # Root application component
├── components/                # Vue components (auto-imported)
│   ├── atoms/                 # Small, reusable UI elements
│   │   ├── button.vue        # Custom button component
│   │   ├── heading.vue        # Dynamic heading component (h1-h6)
│   │   └── link.vue           # Custom link wrapper for NuxtLink
│   ├── globals/               # Global layout components
│   │   ├── banner.vue         # Site banner with contact and account info
│   │   ├── footer.vue         # Site footer with more resources
│   │   ├── header.vue         # Site header with navigation
│   │   └── navigation.vue     # Main navigation menu
├── composables/               # Vue composables (auto-imported)
│   └── useSupabase.ts         # Supabase client with helper methods
├── layouts/                   # Page layouts
│   └── default.vue            # Default page layout wrapper
├── pages/                     # File-based routing
│   ├── index.vue              # Homepage (/)
│   ├── about.vue              # About page (/about)
│   └── inventory.vue          # Inventory page (/inventory)
├── public/                    # Static assets
│   └── gob-logo.png           # Site logo
├── types/                     # TypeScript type definitions (auto-imported)
│   └── index.ts               # Component props and domain types
├── python/                    # Web scraping scripts
│   ├── main.py                # Main scraping script
│   └── requirements.txt       # Python dependencies
├── .env.example               # Environment template
└── nuxt.config.ts             # Nuxt configuration
```

## Component Organization

This project loosely follows atomic design principles for component organization:

### **Atoms** (`/components/atoms/`)
Small, reusable UI elements that can't be broken down further:
- `heading.vue` - Dynamic heading component that renders h1-h6 based on props
- `link.vue` - Custom link wrapper with active state and styling

### **Globals** (`/components/globals/`)
Layout components that appear across multiple pages:
- `header.vue` - Site header with logo and navigation
- `navigation.vue` - Main navigation menu

### **Component Naming Convention**
- Prefix components with their domain: `GlobalsHeader`, `AtomsHeading`

### **TypeScript Integration**
All components use TypeScript with shared type definitions found in `/types/index.ts`.

#### Example
```typescript
// types/index.ts
export interface HeadingProps {
  level?: "1" | "2" | "3" | "4" | "5" | "6"
  title?: string
}

// Component usage
const props = withDefaults(defineProps<HeadingProps>(), {
  level: "1",
  title: "Default Title"
})
```

## Data Pipeline

1. **Scraping**: Python script extracts game data from GOB Retail website
2. **Storage**: Data is stored in Supabase database with JSON backups
3. **Display**: Nuxt.js frontend displays inventory via the Inventory page

## Security Features

- Environment variables for sensitive credentials
- Git-ignored `.env` files and data backups
- Supabase Row Level Security (RLS)
- Input validation and sanitization

## Troubleshooting

### Common Issues

**Missing environment variables**
- Ensure `.env` file exists and contains all required variables
- Restart development server after changes

**Python import errors**
- Activate virtual environment: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

**Supabase connection errors**
- Verify URL and key in `.env` file
- Check Supabase project status and network connectivity

## Deployment

### Production Build
```bash
bun run build
```

### Environment Variables
Set the following in your hosting platform:
- `SUPABASE_URL`
- `SUPABASE_KEY` 
- `NODE_ENV=production`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Copy `.env.example` to `.env` and configure
4. Make your changes
5. Test thoroughly
6. Submit a pull request

## Documentation/Sources

- [Nuxt.js Documentation](https://nuxt.com/docs)
- [Supabase Documentation](https://supabase.com/docs)
- [Semrush Intergalactic Design System](https://intergalactic.semrush.com/)

## License

This project is for educational and portfolio purposes.