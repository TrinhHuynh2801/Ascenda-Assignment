from dataclasses import dataclass

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