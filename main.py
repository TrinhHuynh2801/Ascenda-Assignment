from services.hotels_service import HotelsService
from suppliers.acme import Acme
from suppliers.patagonia import Patagonia
from suppliers.paperflies import Paperflies
import json
import argparse

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
    svc = HotelsService()
    svc.merge_and_save(all_supplier_data)
    
    # # Fetch filtered data
    filtered = svc.find(hotel_ids, destination_ids)

    # Return as json
    # return json.dumps(all_supplier_data, default=vars, indent=2) 
    
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