from models.hotels import Hotel,Amenities,Images,Location,Image
from utils.data_select import *
class HotelsService:  
    def select_best_data(self, mergedHotel):
        best_hotels_data = []
        for hotel in mergedHotel:
            best_hotel = Hotel(
                id=hotel["id"],
                destination_id=hotel["destination_id"],
                name=max(hotel["name"], key=len, default=""),  # Choose the longest name
                location=Location(
                    lat=hotel["location"]["lat"],
                    lng=hotel["location"]["lng"],
                    address=select_most_occurrence(hotel["location"]["address"]),  
                    city=select_most_occurrence(hotel["location"]["city"]),
                    country=select_most_occurrence(hotel["location"]["country"]),
                ),
                description=max(hotel["description"], key=len, default=""),
                amenities=Amenities(
                    general=select_amenities(hotel["amenities"]["general"]),  
                    room= select_amenities(hotel["amenities"]["room"]),
                ),
                images=Images(
                    rooms=select_images(hotel["images"]["rooms"]),
                    site=select_images(hotel["images"]["site"]),
                    amenities=select_images(hotel["images"]["amenities"])
                ),
                booking_conditions=select_book_condition(hotel["booking_conditions"])
            ),
            best_hotels_data.extend(best_hotel)
        return best_hotels_data

    def merge_and_save(self, supplier_data): 
        hotels_map = {}
        for hotel in supplier_data:
            key = f"{hotel.id}-{hotel.destination_id}"
            if key not in hotels_map:
                hotels_map[key] = {
                "id": hotel.id,
                "destination_id": hotel.destination_id,
                "name": [hotel.name] if hotel.name else [],
                "location": {
                    "lat": hotel.location.lat,
                    "lng": hotel.location.lng,
                    "address": [hotel.location.address] if hotel.location.address else [],
                    "city": [hotel.location.city] if hotel.location.city else [],
                    "country": [hotel.location.country] if hotel.location.country else [],
                },
                "description": [hotel.description] if hotel.description else [],
                "amenities": {
                    "general": hotel.amenities.general,
                    "room": hotel.amenities.room,
                },
                "images": {
                    "rooms": hotel.images.rooms,
                    "site": hotel.images.site,
                    "amenities": hotel.images.amenities,
                },
                "booking_conditions": hotel.booking_conditions,
            }
            else:
                existing_hotel = hotels_map[key]

                # Merge location
                existing_hotel["location"]["lat"] = hotel.location.lat if hotel.location.lat > existing_hotel["location"]["lat"] else existing_hotel["location"]["lat"]
                existing_hotel["location"]["lng"] = hotel.location.lng if hotel.location.lng > existing_hotel["location"]["lng"] else existing_hotel["location"]["lng"]
                if (hotel.location.address):
                    existing_hotel["location"]["address"].append(hotel.location.address) 
                if (hotel.location.city):
                    existing_hotel["location"]["city"].append(hotel.location.city)
                if (hotel.location.country):
                    existing_hotel["location"]["country"].append(hotel.location.country)

                # Merge description
                if hotel.description:
                    existing_hotel["description"].append(hotel.description)

                # Merge amenities
                existing_hotel["amenities"]["general"] += hotel.amenities.general
                existing_hotel["amenities"]["room"] += hotel.amenities.room

                # Merge images
                existing_hotel["images"]["rooms"].extend(hotel.images.rooms)
                existing_hotel["images"]["site"].extend(hotel.images.site)
                existing_hotel["images"]["amenities"].extend(hotel.images.amenities)

                # Merge booking conditions
                existing_hotel["booking_conditions"] += hotel.booking_conditions
        # Return the values of the hotels_map dictionary as a list
        return (hotels_map.values())


    def find(self, hotel_ids, destination_ids):
        return