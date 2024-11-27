from dataclasses import dataclass
import json
import argparse

import requests

@dataclass
class Hotel:
    id: str
    destination_id: str
    name: str
    description: str
    location: Location
    amenities: Amenities
    images: Images
    booking_conditions: list[str]

class BaseSupplier:
    def endpoint():
        """URL to fetch supplier data"""

    def parse(obj: dict) -> Hotel:
        """Parse supplier-provided data into Hotel object"""

    def fetch(self):
        url = self.endpoint()
        resp = requests.get(url)
        return [self.parse(dto) for dto in resp.json()]


class Acme(BaseSupplier):
    @staticmethod
    def endpoint():
        return 'https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme'

    @staticmethod
    def parse(dto: dict) -> Hotel:
        return Hotel(
            id=dto['Id'],
            destination_id=dto['DestinationId'],
            name=dto['Name'],
  
        )


def fetch_hotels(hotel_ids, destination_ids):
    # Write your code here

    suppliers = [
        Acme(),
        Paperflies(),
        Patagonia(),
    ]

    # Fetch data from all suppliers
    all_supplier_data = []
    for supp in suppliers:
        all_supplier_data.extend(...)

    # Merge all the data and save it in-memory somewhere
    svc = HotelsService()
    svc.merge_and_save(all_supplier_data)

    # Fetch filtered data
    filtered = svc.find(hotel_ids, destination_ids)

    # Return as json
    return json.dumps()
    
def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("hotel_ids", type=str, help="Hotel IDs")
    parser.add_argument("destination_ids", type=str, help="Destination IDs")
    
    # Parse the arguments
    args = parser.parse_args()
    
    hotel_ids = args.hotel_ids
    destination_ids = args.destination_ids
    
    result = fetch_hotels(hotel_ids, destination_ids)
    print(result)

if __name__ == "__main__":
    main()