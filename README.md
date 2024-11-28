# Ascenda-Assignment

## Features

- Fetch raw data from suppliers.
- Clean data and merge base on `hotel_ids`.
- Select the best data after merge.
- Filter base on `hotel_ids` and `destination_ids`.

## Details

- Merge data using a hash map for unique `hotel_ids` if the key(`hotel_ids`) not exist add to map, if not merge the data.
- Cleaning the data:
  - Remove special characters, remove extra spaces and remove null values.
  - `amenities`: Change all to lowercase.
- Select the data:
  - `name`, `description`: Choose the longest name.
  - `location`: Prioritity the times that value appears.
  - `amenities`, `images`, `booking_conditions`: Remove duplicates.
