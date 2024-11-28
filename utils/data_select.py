
from utils.data_cleaning import *

def select_most_occurrence(data):
    data_map = {}
    max_occurrence = 0
    selected_data = data[0]

    # Count the occurrences of each item
    for item in data:
        key = str(item)
        data_map[key] = data_map.get(key, 0) + 1

    # Find the data with the most occurrences
    for key, occurrence in data_map.items():
        item = int(key) if key.isdigit() else key
        # If appear more than max replace select data
        if occurrence > max_occurrence:
            max_occurrence = occurrence
            selected_data = item
        # Else occurrence same then compare len 
        elif occurrence == max_occurrence:
            # Compare as strings for length
            current_as_string = str(item)
            selected_as_string = str(selected_data)

            if len(current_as_string) > len(selected_as_string):
                selected_data = item

    # Convert back to number if the input was entirely numbers
    if isinstance(data[0], int) and isinstance(selected_data, str) and selected_data.isdigit():
        return int(selected_data)
    return selected_data

def clean_amenity(amenity: str) -> str:
    # Remove special characters and extra spaces, convert to lowercase
    return remove_special_and_lower(amenity)

def select_amenities(amenities):
    cleaned_amenities = [clean_amenity(amenity) for amenity in amenities]
    unique_amenities  = {}
    for amenity in cleaned_amenities:
        key = clean_string(amenity)
        if key not in unique_amenities:
            unique_amenities[key] = amenity
    return list(unique_amenities.values())

def select_book_condition(booking_conditions):
    cleaned_conds = [remove_special_chars(cond) for cond in booking_conditions]
    unique_booking_conds = {}
    for cond in cleaned_conds:
        key = clean_string(cond)
        if key not in unique_booking_conds:
            unique_booking_conds[key] = cond
    return list(unique_booking_conds.values())

def select_images(images):
    seen = set()
    unique_images = []
    for image in images:
        if image.link not in seen:
            unique_images.append(image)
            seen.add(image.link)
    return unique_images