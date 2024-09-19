import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define URLs dictionary
urls = {
    "9780000012494": "https://www.bol.com/be/nl/p/molly-moon-stops-the-world/1001004009720048/",
    "9780001386440": "https://www.bol.com/be/nl/p/rage-of-angels-2-tapes/1001004011844261/",
    "9780001713109": "https://www.bol.com/be/nl/p/animal-riddles/1001004004721799/",
    "9780001713246": "https://www.bol.com/be/nl/p/put-me-in-the-zoo/1001004001107927/",
    "9780001714533": "https://www.bol.com/be/nl/p/the-berenstain-bears-on-the-moon/1001004001054492/",
    "9780001714540": "https://www.bol.com/be/nl/p/wings-on-things/1001004001207338/",
    "9780001720619": "https://www.bol.com/be/nl/p/the-cat-in-the-hat-great-big-flap-book/1001004001125483/",
    "9780001831797": "https://www.bol.com/be/nl/p/the-voyage-of-the-dawn-treader/1001004001054506/",
    "9780001837393": "https://www.bol.com/be/nl/p/brambly-hedge-autumn-story/1001004001243340/",
    "9780001840263": "https://www.bol.com/be/nl/p/the-four-seasons-of-brambly-hedge/1001004001054470/",
    "9780001840867": "https://www.bol.com/be/nl/p/the-high-hills/1001004001253686/",
    "9780001844421": "https://www.bol.com/be/nl/p/the-magician-s-nephew/1001004001054472/",
    "9780001854338": "https://www.bol.com/be/nl/p/fantastic-mr-fox/9300000035381342/",
    "9780001856875": "https://www.bol.com/be/nl/p/dear-olly/1001004001125548/",
    "9780001857339": "https://www.bol.com/be/nl/p/fire-and-hemlock/1001004001147126/",
    "9780001944923": "https://www.bol.com/be/nl/p/bumper-bk-blyton-str/1001004011844263/",
    "9780001951280": "https://www.bol.com/be/nl/p/castle/9300000123486141/",
    "9780001981188": "https://www.bol.com/be/nl/p/a-goodnight-kind-of-feeling/1001004001080884/",
    "9780001982079": "https://www.bol.com/be/nl/p/zoom/1001004001221772/",
    "9780001983571": "https://www.bol.com/be/nl/p/learn-with-paddington-omnibus/1001004006074987/",
    "9780001984004": "https://www.bol.com/be/nl/p/paddington-s-party-tricks/1001004001379748/",
    "9780001984240": "https://www.bol.com/be/nl/p/today-i-feel-silly/1001004001109923/",
    "9780002000178": "https://www.bol.com/be/nl/p/falaise/9200000016939557/",
    "9780002000192": "https://www.bol.com/be/nl/p/journey-to-the-source-of-the-nile/1001004000921315/",
    "9780002000390": "https://www.bol.com/be/nl/p/family-wisdom-from-the-monk-who-sold-his-ferrari/1001004000625436/",
    "9780002000604": "https://www.bol.com/be/nl/p/wolves-among-sheep/9200000035940478/",
    "9780002000987": "https://www.bol.com/be/nl/p/ancient-mariner/9200000027919882/",
    "9780002005104": "https://www.bol.com/be/nl/p/dreadful-water-shows-up/9200000031737987/",
    "9780002005555": "https://www.bol.com/be/nl/p/a-blade-of-grass/9200000027926338/",
    "9780002006705": "https://www.bol.com/be/nl/p/hemingway-in-africa/1001004001987410/",
    "9780002006873": "https://www.bol.com/be/nl/p/the-greatness-guide-book-2/9200000063717944/",
    "9780002006903": "https://www.bol.com/be/nl/p/october/1001004010596613/",
    "9780002007184": "https://www.bol.com/be/nl/p/woolf-in-ceylon/1001004002624483/",
    "9780002007245": "https://www.bol.com/be/nl/p/causeway/9200000015767739/",
    "9780002008075": "https://www.bol.com/be/nl/p/town-house/9200000018102973/",
    "9780002008471": "https://www.bol.com/be/nl/p/bad-bridesmaid/9200000015767993/",
    "9780002008815": "https://www.bol.com/be/nl/p/at-a-loss-for-words/1001004008703773/",
    "9780002114981": "https://www.bol.com/be/nl/p/last-of-the-nuba-the/1001004001054177/",
    "9780002118477": "https://www.bol.com/be/nl/p/the-third-wave/9200000082606117/",
    "9780002119528": "https://www.bol.com/be/nl/p/the-world-at-war/9300000083241914/",
    "9780002150842": "https://www.bol.com/be/nl/p/pushkin/1001004001662537/",
    "9780002151399": "https://www.bol.com/be/nl/p/the-companion-guide-to-florence/9200000066545416/",
    "9780002151658": "https://www.bol.com/be/nl/p/dreams-of-india/9200000067191627/",
    "9780002151962": "https://www.bol.com/be/nl/p/throne-of-gold/9300000006437851/",
    "9780002153560": "https://www.bol.com/be/nl/p/in-search-of-churchill/9200000070351167/",
    "9780002154123": "https://www.bol.com/be/nl/p/france/1001004001159733/",
    "9780002158688": "https://www.bol.com/be/nl/p/history-of-the-20th-century/1001004000970242/",
    "9780002158961": "https://www.bol.com/be/nl/p/faust-s-metropolis/9300000033547641/",
    "9780002159616": "https://www.bol.com/be/nl/p/australia-wide/9200000066545208/",
    "9780002160780": "https://www.bol.com/be/nl/p/the-best-of-david-hamilton/9300000095470282/",
    "9780002160940": "https://www.bol.com/be/nl/p/the-dance-art-and-ritual-of-africa/9300000113620773/",
    "9780002161947": "https://www.bol.com/be/nl/p/the-life-of-my-choice/1001004001270335/",
    "9780002161978": "https://www.bol.com/be/nl/p/book-of-railway-journeys/9200000080436581/",
    "9780002163651": "https://www.bol.com/be/nl/p/kiri/9200000070351151/",
    "9780002163705": "https://www.bol.com/be/nl/p/nomads-of-niger/1001004001212778/",
    "9780002164696": "https://www.bol.com/be/nl/p/lichfield-on-photography/9200000067515783/",
    "9780002167352": "https://www.bol.com/be/nl/p/south-of-france/1001004006103406/",
    "9780002171892": "https://www.bol.com/be/nl/p/four-hundred-years-of-fashion/9200000080742872/",
    "9780002175357": "https://www.bol.com/be/nl/p/an-illustrated-history-of-england/9200000066545274/",
    "9780002175760": "https://www.bol.com/be/nl/p/new-zealand/9200000051827565/",
    "9780002177085": "https://www.bol.com/be/nl/p/theodore-rex/1001004001465540/",
    "9780002177122": "https://www.bol.com/be/nl/p/a-day-in-the-life-of-the-soviet-union/9200000055285814/",
    "9780002177597": "https://www.bol.com/be/nl/p/the-racegoers-encyclopedia/9200000087132572/",
    "9780002177702": "https://www.bol.com/be/nl/p/more-bedside-bridge/9200000067191613/",
    "9780002178242": "https://www.bol.com/be/nl/p/rainbow-warrior/1001004001270285/",
    "9780002178415": "https://www.bol.com/be/nl/p/botham-s-century/1001004001434877/"
}


# List to hold the results
results = []

# Loop through each URL
for isbn, url in urls.items():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Extract title and price
    title = soup.find('h1', class_='page-heading').get_text(strip=True) if soup.find('h1', class_='product-title') else 'N/A'
    price = soup.find('span', class_='promo-price').get_text(strip=True) if soup.find('span', class_='promo-price') else 'N/A'
    price1 = soup.find('span', class_='promo-price__fraction').get_text(strip=True) if soup.find('span', class_='promo-price__fraction') else 'N/A'
    
    # Add results to list
    results.append({
        'ISBN': isbn,
        'Title': title,
        'Price': price[:2] + ',' + price[2:4]
    })

# Create a DataFrame
df = pd.DataFrame(results)

# Save DataFrame to CSV
df.to_csv('books_info.csv', index=False)

print("Data saved to books_info.csv")
