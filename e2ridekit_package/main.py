import argparse
import pandas as pd
from .functions import calculate_Deadhead, calculate_deadheadEmission, calculate_Distance, \
    calculate_traveledEmission, calculate_ev_metrics, filter_trips_by_date, get_random_samples


def read_config(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    config = {}
    for line in lines:
        key, value = line.strip().split('=')
        config[key] = value

    return config


def main():
    parser = argparse.ArgumentParser(description='RideAustin calculations')
    parser.add_argument('-d', action='store_true', help='Compute deadhead miles')
    parser.add_argument('-de', action='store_true', help='Compute deadhead emissions')
    parser.add_argument('-t', action='store_true', help='Compute traveled distance')
    parser.add_argument('-te', action='store_true', help='Compute traveled emissions')
    parser.add_argument('-i', '--input', type=str, help='Input file path')
    parser.add_argument('-o', '--output', type=str, help='Output file path')
    parser.add_argument('-ev', nargs=2, type=float, help='Electric vehicle settings: percentage grid_intensity')
    parser.add_argument('-sd', '--start-date', type=str, help='Start date in YYYY-MM-DD format')
    parser.add_argument('-ed', '--end-date', type=str, help='End date in YYYY-MM-DD format')
    parser.add_argument('-nd', '--num-drivers', type=int, help='Number of random drivers to select')
    parser.add_argument('-n', '--num-samples-per-driver', type=int, help='Number of random samples per driver to get')

    args = parser.parse_args()

    if args.input is None:
        print("Please provide an input file using the -i/--input flag.")
        return

    if args.output is None:
        print("Please provide an output file using the -o/--output flag.")
        return

    dataset_a = pd.read_csv(args.input)
    trips = pd.DataFrame(dataset_a)
    trips = trips.sort_values(by=['started_on'])

    if args.d:
        trips['deadhead_miles (km)'] = calculate_Deadhead(trips)

    if args.de:
        trips['deadhead_emission (gCO2)'] = calculate_deadheadEmission(trips)

    if args.t:
        trips['traveled_distance (km)'] = trips.apply(lambda row: calculate_Distance(
            row['end_location_lat'], row['end_location_long'],
            row['start_location_lat'], row['start_location_long']) if not pd.isnull(row['end_location_lat']) else -1,
                                                      axis=1)
    if args.te:
        trips['traveled_emission (gCO2)'] = calculate_traveledEmission(trips)

    if args.ev:
        if len(args.ev) != 2:
            print("Please provide both electric vehicle percentage and grid intensity.")
            return

        ev_percentage, grid_intensity = args.ev
        trips = calculate_ev_metrics(trips, ev_percentage, grid_intensity)

    if args.start_date and args.end_date:
        trips = filter_trips_by_date(trips, args.start_date, args.end_date)

    if args.num_drivers and args.num_samples_per_driver:
        trips = get_random_samples(trips, args.num_drivers, args.num_samples_per_driver)
    else:
        print("Please provide both the number of drivers (-d) and the number of samples per driver (-n).")

    trips.to_csv(args.output, index=False)
    print("Calculations completed. Results saved to:", args.output)


if __name__ == '__main__':
    main()
