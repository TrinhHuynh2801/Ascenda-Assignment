class HotelsService:
    def __init__(self):
        self.hotels = [];    
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
        print(hotels_map.values())
        return list(hotels_map.values())

    def find(self, hotel_ids, destination_ids):
        return