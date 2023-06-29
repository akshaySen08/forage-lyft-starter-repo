from battery import Battery
from utils import add_years_to_date

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        # once every 4 years
        new_date_of_service = add_years_to_date(self.last_service_date, 4)
        if(new_date_of_service < self.current_date):
            # needs service
            return True
        else:
            return False