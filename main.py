import requests
from bs4 import BeautifulSoup
import pandas as pd


links = [
    {"ISBN": "9780000012494", "URL": "https://www.bol.com/be/nl/p/molly-moon-stops-the-world/1001004009720048/"},
    
]

data = []

def check_link_and_get_price(link):
    try:
        response = requests.get(link["URL"])
        if response.status_code == 200:
            print(f"الرابط {link['URL']} شغال.")
            soup = BeautifulSoup(response.content, 'html.parser')

            
            price_tag = soup.find('span', class_='price-block__highlight') 

            if price_tag:
                price = price_tag.get_text(strip=True)
                return price
            else:
                print(f"لم يتم العثور على سعر في {link['URL']}.")
                return None
        else:
            print(f"الرابط {link['URL']} غير شغال. رمز الحالة: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"حدث خطأ: {e}")
        return None


for link in links:
    price = check_link_and_get_price(link)
    data.append({"ISBN": link["ISBN"], "URL": link["URL"], "Price": price})


df = pd.DataFrame(data)
df.to_excel("product_prices.xlsx", index=False)

print("تم حفظ البيانات في ملف Excel بنجاح!")

