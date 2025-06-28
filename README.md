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
├── pages/           # Nuxt.js pages and routes
├── composables/     # Vue composables (including useSupabase)
├── public/          # Static assets
├── python/          # Web scraping scripts
│   ├── main.py      # Main scraping script
│   └── requirements.txt
├── .env.example     # Environment template
└── nuxt.config.ts   # Nuxt configuration
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