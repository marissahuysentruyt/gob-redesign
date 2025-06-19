from supabase import create_client, Client
import requests
from bs4 import BeautifulSoup
import re
import unicodedata
import json
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in environment variables")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# 🔎 Test query (lists the first item in the inventory table)
def test_connection():
    response = supabase.table("inventory").select("*").limit(1).execute()
    print(response)

# Run the test
test_connection()

# Utility functions
def normalize_text(text):
    return unicodedata.normalize("NFKC", text).replace("\xa0", " ").replace("\r\n", " ").strip()

def clean_description(text):
    return re.sub(r'Buy.*For Only.*$', '', text, flags=re.IGNORECASE).strip()

def compress_spaces(text):
    return re.sub(r"\s+", " ", text).strip()

# Web scraping setup
def setup_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    html = res.text
    return BeautifulSoup(html, 'html.parser')

# Data extraction functions
def get_game_title(soup):
    title_tag = soup.find("title")
    return title_tag.get_text(strip=True) if title_tag else None

def get_price(soup, label="Our Price"):
    try:
        all_td_tags = soup.find_all("td")
        for i, td in enumerate(all_td_tags):
            text = td.get_text(strip=True).lower()

            if label.lower() in text:
                parent_row = td.find_parent("tr")
                if not parent_row:
                    continue

                td_cells = parent_row.find_all("td")
                if len(td_cells) < 2:
                    print(f"⚠️ Not enough <td> cells in row for '{label}'")
                    continue

                # Assume price is in the second <td>
                value_cell = td_cells[1]
                price_text = value_cell.get_text(strip=True)

                match = re.search(r"\$?([\d]+\.\d{2})", price_text)
                if match:
                    price = float(match.group(1))
                    return price

        print(f"❌ '{label}' not found or price missing")
        return None

    except Exception as e:
        print(f"❌ Error extracting {label} price: {e}")
        return None

def get_in_stock(soup):
    try:
        all_b_tags = soup.find_all("b")

        for i, b in enumerate(all_b_tags):
            label = b.get_text(strip=True).lower()

            if label == "in stock:":
                parent_row = b.find_parent("tr")
                if not parent_row:
                    print("⚠️ No parent <tr> found for In Stock")
                    continue

                td_cells = parent_row.find_all("td")
                if len(td_cells) < 2:
                    print("⚠️ Not enough <td> cells in In Stock row")
                    continue

                stock_text = td_cells[1].get_text(strip=True)

                try:
                    stock_count = int(stock_text)
                    return stock_count
                except ValueError:
                    print(f"⚠️ Unable to parse stock count from: '{stock_text}'")
                    return None

        print("❌ 'In Stock:' label not found")
        return None

    except Exception as e:
        print(f"❌ Error extracting In Stock value: {e}")
        return None

def get_game_type(soup):
    try:
        all_b_tags = soup.find_all("b")

        for i, b in enumerate(all_b_tags):
            label = b.get_text(strip=True).lower()

            if label == "game type:":
                parent_row = b.find_parent("tr")
                if not parent_row:
                    print("⚠️ No parent <tr> found for Game Type")
                    continue

                td_cells = parent_row.find_all("td")
                if len(td_cells) < 2:
                    print("⚠️ Not enough <td> cells in Game Type row")
                    continue

                # Extract and clean the second <td>'s text
                game_type = td_cells[1].get_text(strip=True)
                return game_type

        print("❌ 'Game Type:' label not found")
        return None

    except Exception as e:
        print(f"❌ Error extracting Game Type: {e}")
        return None

def get_created_by(soup):
    try:
        all_b_tags = soup.find_all("b")
        for i, b in enumerate(all_b_tags):
            if b.get_text(strip=True).lower() == "by:":
                # Get the parent <td>
                parent_td = b.find_parent("td")
                if not parent_td:
                    print("⚠️ No parent <td> found")
                    return ""

                # Look for the next sibling <td> with the creator name
                next_td = parent_td.find_next_sibling("td")
                if next_td:
                    creators = next_td.get_text(strip=True)
                    return creators
                else:
                    print("⚠️ No next <td> found after 'By:'")
                    return ""

        print("❌ No 'By:' <b> tag found")
        return ""

    except Exception as e:
        print(f"❌ Error in get_created_by(): {e}")
        return ""

def get_image_path(soup):
    try:
        img_tags = soup.find_all("img")
        game_title = get_game_title(soup)

        for i, img in enumerate(img_tags):
            src = img.get("src")
            alt = img.get("alt")

            if alt and game_title and alt.strip().lower() == game_title.strip().lower():
                return src

        print("⚠️ No suitable game image found.")
        return None

    except Exception as e:
        print(f"❌ Error in get_image_path: {e}")
        return None

def get_game_description(soup):
    try:
        font_tags = soup.find_all("font")

        for font in font_tags:
            if font.get_text(strip=True).lower() == "description":
                # Find the top-level <p> that contains this <font>
                parent_p = font.find_parent("p")
                if parent_p:
                    # Get the full text of this <p>, then remove "Description" label
                    full_text = parent_p.get_text(strip=True)
                    label = font.get_text(strip=True)
                    cleaned = full_text.replace(label, "").strip()

                    if cleaned:
                        return cleaned
                    else:
                        # Try fallback to the next <p> if cleaned was empty
                        next_p = parent_p.find_next_sibling("p")
                        if next_p:
                            desc = next_p.get_text(strip=True)
                            return desc
                        else:
                            print("⚠️ No next <p> found after Description label")
                            return ""

        print("❌ No <font>Description</font> tag found")
        return ""

    except Exception as e:
        print(f"❌ Error in get_game_description: {e}")
        return ""

def get_item_condition(url):
    return "Used" if "usedproduct=1" in url else "New"

# Parse sitemap
import xml.etree.ElementTree as ET

def parse_sitemap(file_path):
    print("Parsing sitemap...")
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    urls = [url.find('ns:loc', namespaces).text for url in root.findall('ns:url', namespaces) if url.find('ns:loc', namespaces) is not None]
    print(f"Found {len(urls)} URLs in sitemap.")
    return urls

# Scrape for data
def extract_game_data(url):
    print(f"Scraping {url}")
    try:
        soup = setup_soup(url)

        data = {
            "name": normalize_text(get_game_title(soup) or ""),
            "price": get_price(soup, "Our price"),
            "in_stock": get_in_stock(soup),
            "type": normalize_text(compress_spaces(get_game_type(soup) or "")),
            "created_by": normalize_text(get_created_by(soup)),
            "image_path": get_image_path(soup),
            "description": normalize_text(clean_description(get_game_description(soup))),
            "item_condition": get_item_condition(url),
            "msrp": get_price(soup, "MSRP"),
        }

        return data

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Save to file
def save_to_json(data, filename=None):
    import os

    # Ensure the .data/content directory exists
    content_dir = ".data/content"
    os.makedirs(content_dir, exist_ok=True)

    if not filename:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"gobretail_products_{timestamp}.json"

    # Add the directory path to filename
    filepath = os.path.join(content_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Data saved to {filepath}")

urls = parse_sitemap("./python/sitemap.xml")

product_urls = [url for url in urls if url and "Gamesinfo.php" in url and "gobitemcode=" in url]

sample_urls = product_urls[:6]  # test with a small number first

# Step 2: Collect all data
all_products = []

for url in sample_urls:
    data = extract_game_data(url)
    if data:
        all_products.append(data)
    print(data)  # Optional: for real-time feedback

# save_to_json(all_products)

# # Push each record into the table
# for i in range(0, len(all_products), 50):
#     try:
#         # Insert in chunks of 50
#         batch = all_products[i:i + 50]
#         supabase.table("inventory").insert(batch).execute()
#         print(f"✅ Inserted {len(batch)} products.")
#     except Exception as e:
#         print(f"❌ Error inserting batch starting at index {i}: {e}")
