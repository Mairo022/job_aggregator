import time

from constants import LOCATIONS_AVAILABLE, CACHE_LIFESPAN
from jobs.LocationHandler import LocationHandler

location_handlers: dict[int, LocationHandler] = {location: LocationHandler() for location in LOCATIONS_AVAILABLE}


def get_jobs(start, location, category):
    jobs = location_handlers.get(location).get_jobs(start, location, category)
    return jobs


def cleanup_location_handlers() -> None:
    while True:
        time.sleep(CACHE_LIFESPAN)
        # print("Cleaning location handlers")
        for handler in location_handlers.values():
            handler.cleanup()
