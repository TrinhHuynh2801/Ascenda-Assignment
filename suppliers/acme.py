from suppliers.base import BaseSupplier
from models.hotels import Hotel,Amenities,Images,Location
from utils.data_cleaning import trim, remove_special_chars, upper_and_trim

class Acme(BaseSupplier):
    @staticmethod
    def endpoint():
        return "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme"

    @staticmethod
    def parse(dto: dict) -> Hotel:
        return Hotel(
            id=dto["Id"],
            destination_id=dto["DestinationId"],
            name=trim(dto["Name"] or ""),
            location=Location(
            lat=float(dto.get("Latitude", 0.0) or 0.0),  
            lng=float(dto.get("Longitude", 0.0) or 0.0),  
                address=upper_and_trim(dto.get("Address", "") or ""),
                city=upper_and_trim(dto.get("City", "") or ""),
                country=upper_and_trim(dto.get("Country", "") or ""),
            ),
            description=remove_special_chars(dto.get("Description", "")  or ""),
            amenities=Amenities(
                general=dto.get("Facilities", []) or [],
                room=[],
            ),
            images=Images(
                rooms=[],
                site=[],
                amenities=[],
            ),
            booking_conditions=[],
        )