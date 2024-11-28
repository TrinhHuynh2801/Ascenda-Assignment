from suppliers.base import BaseSupplier
from models.hotels import Hotel,Amenities,Images,Location,Image
from utils.data_cleaning import trim, remove_special_chars, upper_and_trim

class Paperflies(BaseSupplier):
    @staticmethod
    def endpoint():
        return "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies"

    @staticmethod
    def parse(dto: dict) -> Hotel:
        return Hotel(
            id=dto["hotel_id"],
            destination_id=dto["destination_id"],
            name=trim(dto["hotel_name"] or ""),
            location=Location(
            lat=float(dto.get("Latitude", 0.0) or 0.0),  # Convert to float or default to 0.0
            lng=float(dto.get("Longitude", 0.0) or 0.0),  # Convert to float or default to 0.0
                address = upper_and_trim(dto.get("location", {}).get("address", "") or ""),
                city=upper_and_trim(dto.get("city", "") or ""),
                country=upper_and_trim(dto.get("location", {}).get("country", "") or ""),
            ),
            description=remove_special_chars(dto.get("details", "") or ""),
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
            booking_conditions=dto["booking_conditions"] or [],
        )
