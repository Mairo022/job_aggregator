import logging
import time

from constants import LOCATIONS_AVAILABLE, CACHE_LIFESPAN, CATEGORIES, CATEGORY_IT_LOCATIONS
from jobs.LocationHandler import LocationHandler

location_handlers_no_category: dict[int, LocationHandler] = \
    {location: LocationHandler() for location in LOCATIONS_AVAILABLE}

location_handlers_it: dict[int, LocationHandler] = \
    {location: LocationHandler() for location in CATEGORY_IT_LOCATIONS}


def get_jobs(start, location, category):
    match category:
        case CATEGORIES.ALL.value:
            return location_handlers_no_category.get(location).get_jobs(start, location, category)
        case CATEGORIES.IT.value:
            return location_handlers_it.get(location).get_jobs(start, location, category)
        case _:
            logging.error(f"No matching category: category {category}, location {location}")
            return {}


def cleanup_location_handlers() -> None:
    while True:
        time.sleep(CACHE_LIFESPAN)
        for handler in location_handlers_no_category.values():
            handler.cleanup()
        for handler in location_handlers_it.values():
            handler.cleanup()
