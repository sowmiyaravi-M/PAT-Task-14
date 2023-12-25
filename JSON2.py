import http.client
import json

def get_breweries_by_state(state):
    conn = http.client.HTTPSConnection("api.openbrewerydb.org")
    endpoint = f"/breweries?by_state={state}"
    conn.request("GET", endpoint)
    response = conn.getresponse()
    
    if response.status == 200:
        data = response.read()
        return json.loads(data)
    else:
        print(f"Error fetching data for state {state}")
        return None

def list_breweries_by_state(states):
    for state in states:
        breweries = get_breweries_by_state(state)
        if breweries:
            brewery_names = [brewery['name'] for brewery in breweries]
            print(f"\nBreweries in {state}:")
            print(', '.join(brewery_names))
            print(f"Count of breweries in {state}: {len(breweries)}")

            # Count types of breweries in individual cities
            city_breweries = {}
            for brewery in breweries:
                city = brewery.get('city', 'Unknown')
                brewery_type = brewery.get('brewery_type', 'Unknown')
                city_breweries[city] = city_breweries.get(city, {})
                city_breweries[city][brewery_type] = city_breweries[city].get(brewery_type, 0) + 1

            print(f"\nTypes of breweries in {state} cities:")
            for city, types_count in city_breweries.items():
                print(f"{city}: {types_count}")

            # Count and list breweries with websites
            websites_breweries = [brewery['name'] for brewery in breweries if 'website_url' in brewery and brewery['website_url']]
            print(f"\nBreweries in {state} with websites:")
            print(', '.join(websites_breweries))

if __name__ == "__main__":
    # Define the states you are interested in
    target_states = ['Alaska', 'Maine', 'New York']

    list_breweries_by_state(target_states)

