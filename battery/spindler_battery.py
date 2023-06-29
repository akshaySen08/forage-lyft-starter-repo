from abc import ABC
from utils import add_years_to_date

class SpindlerBattery(ABC):
    def __init__(self, last_service_date, current_date) :
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        # on every 2 years
        new_date_of_service = add_years_to_date(self.last_service_date, 2)
        if(new_date_of_service < self.current_date):
            # needs service
            return True
        else:
            return False
    