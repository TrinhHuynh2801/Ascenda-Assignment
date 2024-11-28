from suppliers.base import BaseSupplier
from models.hotels import Hotel,Amenities,Images,Location,Image
from utils.data_cleaning import trim, remove_special_chars, upper_and_trim

class Patagonia(BaseSupplier):
    @staticmethod
    def endpoint():
        return "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/patagonia"

    @staticmethod
    def parse(dto: dict) -> Hotel:
        return Hotel(
            id=dto["id"],
            destination_id=dto["destination"],
            name=trim(dto["name"] or ""),
            location=Location(
            lat=float(dto.get("lat", 0.0) or 0.0),  # Convert to float or default to 0.0
            lng=float(dto.get("lng", 0.0) or 0.0),  # Convert to float or default to 0.0
                address=upper_and_trim(dto.get("address", "") or ""),
                city=upper_and_trim(dto.get("city", "") or ""), #Patagonia supplier don't have city field
                country=upper_and_trim(dto.get("country", "") or ""), #Patagonia supplier don't have country field
            ),
            description=remove_special_chars(dto.get("info", "") or ""),
            amenities=Amenities(
                general=dto.get("amenities", []) or [],
                room=dto["amenities"] or [],
            ),
            images=Images(
                rooms=[
                    Image(link=image["url"], description=image.get("description", ""))
                    for image in dto.get("images", {}).get("rooms", [])  
                ],
                site=[],
                amenities=[
                    Image(link=image["url"], description=image.get("description", ""))
                    for image in dto.get("images", {}).get("amenities", [])
                ],
            ),
            booking_conditions=[],
        )
