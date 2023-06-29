from datetime import date


def add_years_to_date(service_date, years_to_add):
    future_date = date.fromordinal(service_date, 365 * years_to_add)
    return future_date
