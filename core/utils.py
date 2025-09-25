# core/utils.py
import requests

def ping_google_sitemap():
    sitemap_url = "https://jobifyworld.com/sitemap.xml"
    try:
        response = requests.get(f"https://www.google.com/ping?sitemap={sitemap_url}")
        if response.status_code == 200:
            print("Successfully pinged Google!")
        else:
            print(f"Failed to ping Google. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error pinging Google: {e}")
