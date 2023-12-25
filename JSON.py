import urllib.request
import json

class CountryInfoFetcher:
    def __init__(self, url):
        self.url = url
        self.country_data = None

    def fetch_data(self):
        try:
            with urllib.request.urlopen(self.url) as response:
                data = response.read().decode('utf-8')
                self.country_data = json.loads(data)
                print("Data successfully fetched.")
        except urllib.error.URLError as e:
            print(f"Failed to fetch data. Error: {e}")

    def display_country_info(self):
        if not self.country_data:
            print("Data not available. Fetch data first.")
            return

        print("Country Information:")
        for country in self.country_data:
            name = country.get('name', {}).get('common', 'N/A')
            currencies = country.get('currencies', {})
            currency_code = next(iter(currencies), 'N/A')
            currency_info = currencies.get(currency_code, {})
            currency_name = currency_info.get('name', 'N/A')
            currency_symbol = currency_info.get('symbol', 'N/A')

            print(f"Country: {name}")
            print(f"Currency: {currency_name}")
            print(f"Currency Symbol: {currency_symbol}")
            print("=" * 30)

    def display_dollar_countries(self):
        if not self.country_data:
            print("Data not available. Fetch data first.")
            return

        dollar_countries = [country for country in self.country_data if 'USD' in country.get('currencies', {})]
        print("Countries with Dollar as currency:")
        for country in dollar_countries:
            print(country.get('name', {}).get('common', 'N/A'))
        print("=" * 30)

    def display_euro_countries(self):
        if not self.country_data:
            print("Data not available. Fetch data first.")
            return

        euro_countries = [country for country in self.country_data if 'EUR' in country.get('currencies', {})]
        print("Countries with Euro as currency:")
        for country in euro_countries:
            print(country.get('name', {}).get('common', 'N/A'))
        print("=" * 30)

# Instantiate the class with the provided URL
url = "https://restcountries.com/v3.1/all"
country_info_fetcher = CountryInfoFetcher(url)

# Fetch data from the URL
country_info_fetcher.fetch_data()

# Display country information
country_info_fetcher.display_country_info()

# Display countries with Dollar as currency
country_info_fetcher.display_dollar_countries()

# Display countries with Euro as currency
country_info_fetcher.display_euro_countries()

