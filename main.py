from dataclasses import dataclass
from utils.data_cleaning import trim, remove_special_chars, upper_and_trim
import json
import argparse
import requests

@dataclass
class Location:
    lat: float
    lng: float
    address: str
    city: str
    country: str


@dataclass
class Amenities:
    general: list[str]
    room: list[str]


@dataclass
class Image:
    link: str
    description: str


@dataclass
class Images:
    rooms: list[Image]
    site: list[Image]
    amenities: list[Image]


@dataclass
class Hotel:
    id: str
    destination_id: str
    name: str
    location: Location
    description: str
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
        return "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme"

    @staticmethod
    def parse(dto: dict) -> Hotel:
        return Hotel(
            id=dto["Id"],
            destination_id=dto["DestinationId"],
            name=trim(dto["Name"]),
            location=Location(
            lat=float(dto.get("Latitude", 0.0) or 0.0),  # Convert to float or default to 0.0
            lng=float(dto.get("Longitude", 0.0) or 0.0),  # Convert to float or default to 0.0
                address=upper_and_trim(dto.get("Address", "")),
                city=upper_and_trim(dto.get("City", "")),
                country=upper_and_trim(dto.get("Country", "")),
            ),
            description=remove_special_chars(dto.get("Description", "")),
            amenities=Amenities(
                general=dto.get("Facilities", []),
                room=[],
            ),
            images=Images(
                rooms=[],
                site=[],
                amenities=[],
            ),
            booking_conditions=[],
        )


class Patagonia(BaseSupplier):
    @staticmethod
    def endpoint():
        return "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/patagonia"

    @staticmethod
    def parse(dto: dict) -> Hotel:
        return Hotel(
            id=dto["id"],
            destination_id=dto["destination"],
            name=dto["name"],
            location=Location(
            lat=float(dto.get("Latitude", 0.0) or 0.0),  # Convert to float or default to 0.0
            lng=float(dto.get("Longitude", 0.0) or 0.0),  # Convert to float or default to 0.0
                address=dto.get("address", ""),
                city=dto.get("city", ""),
                country=dto.get("country", ""),
            ),
            description=dto.get("info", ""),
            amenities=Amenities(
                general=dto.get("amenities", []),
                room=dto["amenities"],
            ),
            images=Images(
                rooms=[
                    Image(link=image["url"], description=image.get("description", ""))
                    for image in dto["images"].get("rooms", [])
                ],
                site=[],
                amenities=[
                    Image(link=image["url"], description=image.get("description", ""))
                    for image in dto["images"].get("amenities", [])
                ],
            ),
            booking_conditions=[],
        )


class Paperflies(BaseSupplier):
    @staticmethod
    def endpoint():
        return "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies"

    @staticmethod
    def parse(dto: dict) -> Hotel:
        return Hotel(
            id=dto["hotel_id"],
            destination_id=dto["destination_id"],
            name=dto["hotel_name"],
            location=Location(
            lat=float(dto.get("Latitude", 0.0) or 0.0),  # Convert to float or default to 0.0
            lng=float(dto.get("Longitude", 0.0) or 0.0),  # Convert to float or default to 0.0
                address=dto.get("location", {}).get("address", ""),
                city=dto.get("City", ""),
                country=dto.get("location", {}).get("country", ""),
            ),
            description=dto.get("details", ""),
            amenities=Amenities(
                general=dto.get("amenities", {}).get("general", []),
                room=dto.get("amenities", {}).get("room", []),
            ),
            images=Images(
                rooms=[
                    Image(link=image["link"], description=image.get("caption", ""))
                    for image in dto["images"].get("rooms", [])
                ],
                site=[
                    Image(link=image["link"], description=image.get("caption", ""))
                    for image in dto["images"].get("site", [])
                ],
                amenities=[],
            ),
            booking_conditions=dto["booking_conditions"],
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
        supplier_data = supp.fetch() 
        all_supplier_data.extend(supplier_data)

    # Merge all the data and save it in-memory somewhere
    # svc = HotelsService()
    # svc.merge_and_save(all_supplier_data)

    # # Fetch filtered data
    # filtered = svc.find(hotel_ids, destination_ids)

    # Return as json
    return json.dumps(all_supplier_data[0], default=vars, indent=2) 
    
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