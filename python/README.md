# Python Web Scraping Setup

This directory contains the Python web scraping script for extracting game data from the GOB Retail website.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Navigate to the python directory:**
   ```bash
   cd python
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables

1. **Copy the environment template:**
   ```bash
   cp ../.env.example ../.env
   ```

2. **Edit the `.env` file** with your actual Supabase credentials:
   ```
   SUPABASE_URL=your_supabase_project_url_here
   SUPABASE_KEY=your_supabase_anon_key_here
   ```

## Usage

### Running the Scraper

```bash
python main.py
```

The script will:
1. Parse the sitemap to find product URLs
2. Extract data from each product page
3. Save a JSON backup to `../.data/content/`
4. Insert the data into your Supabase database

### Script Components

- **`main.py`** - Main scraping script
- **`sitemap.xml`** - Website sitemap for URL discovery
- **`requirements.txt`** - Python dependencies

### Functions

- `extract_game_data(url)` - Main data extraction function
- `setup_soup(url)` - Web scraping setup
- `get_*()` functions - Individual data extractors
- `save_to_json()` - Backup data to JSON
- `parse_sitemap()` - Extract URLs from sitemap

## Data Structure

Each scraped item contains:
- `name` - Game title
- `price` - Current selling price
- `in_stock` - Quantity available
- `type` - Game category (Board Game, TCG, etc.)
- `created_by` - Publisher/creator
- `image_path` - Product image URL
- `description` - Game description
- `item_condition` - New/Used status
- `msrp` - Manufacturer's suggested retail price

## Output

- **JSON Backup**: Saved to `../.data/content/gobretail_products_YYYY-MM-DD_HH-MM-SS.json`
- **Database**: Inserted into Supabase `inventory` table in batches of 50

## Troubleshooting

### Common Issues

1. **Missing dependencies**: Run `pip install -r requirements.txt`
2. **Environment variables not found**: Check your `.env` file exists and has correct values
3. **Supabase connection error**: Verify your URL and key in `.env`
4. **Rate limiting**: The script includes headers to avoid being blocked

### Error Handling

- Individual page scraping errors are logged but don't stop the process
- Database insertion happens in batches with error handling
- JSON backup is always created regardless of database issues

## Development

### Adding New Data Fields

1. Create a new extraction function (e.g., `get_new_field(soup)`)
2. Add it to the data dictionary in `extract_game_data()`
3. Update the database schema if needed

### Testing

You can test with a smaller dataset by uncommenting:
```python
# sample_urls = product_urls[:6]  # test with a small number first
```

## Dependencies

- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- `supabase` - Database client
- `python-dotenv` - Environment variable loading
- `lxml` - XML/HTML parser (faster than default)