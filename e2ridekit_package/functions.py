import pandas as pd
from geopy.distance import great_circle
import numpy as np


def calculate_deadheadEmission(trips):
    emission_row = trips['deadhead_miles (km)'] * trips['CO2 emission (g/km)']
    return emission_row


def calculate_traveledEmission(trips):
    traveled_emission = trips['traveled_distance (km)'] * trips['CO2 emission (g/km)']
    return traveled_emission


def calculate_ev_metrics(trips, ev_percentage, grid_intensity):
    unique_drivers = trips['driver_id'].nunique()
    num_ev_drivers = int(unique_drivers * (ev_percentage / 100))

    ev_driver_ids = np.random.choice(trips['driver_id'].unique(), num_ev_drivers, replace=False)
    ev_indices = trips[trips['driver_id'].isin(ev_driver_ids)].index

    trips.loc[ev_indices, 'CO2 emission (g/km)'] = grid_intensity

    return trips


def filter_trips_by_date(trips, start_date, end_date):
    trips['started_on'] = trips['started_on'].fillna('1970-01-01 00:00:00+00:00')
    trips['started_on'] = pd.to_datetime(trips['started_on'], utc=True)
    start_date = pd.Timestamp(start_date).tz_localize(trips['started_on'].dt.tz)
    end_date = pd.Timestamp(end_date).tz_localize(trips['started_on'].dt.tz) + pd.DateOffset(days=1)

    selected_trips = trips[(trips['started_on'] >= start_date) & (trips['started_on'] <= end_date)]

    return selected_trips


def get_random_samples(trips, num_samples):
    random_samples = trips.sample(num_samples)
    return random_samples


def calculate_Distance(lat1, lon1, lat2, lon2):
    point1 = (lat1, lon1)
    point2 = (lat2, lon2)

    distance = great_circle(point1, point2).km

    return distance


def calculate_Deadhead(trips):
    trips['previous_dropoff_lat'] = trips.groupby('driver_id')['end_location_lat'].shift(1)
    trips['previous_dropoff_lon'] = trips.groupby('driver_id')['end_location_long'].shift(1)

    rows = trips.apply(lambda row: calculate_Distance(
        row['previous_dropoff_lat'], row['previous_dropoff_lon'],
        row['start_location_lat'], row['start_location_long']
    ) if not pd.isnull(row['previous_dropoff_lat']) else 0, axis=1)

    zero_dead_heads = sum(rows == 0)
    num_drivers = len(trips['driver_id'].unique())

    print("Zero dead heads: {0} / {1}".format(zero_dead_heads, len(trips)))
    print("Number of drivers: {0}".format(num_drivers))

    return rows


