
# E2-RideKit

![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen) ![Version](https://img.shields.io/badge/Version-1.0.0-orange) ![Python](https://img.shields.io/badge/Python-3.7%20|%203.8%20|%203.9%20-blue) [![geopy](https://img.shields.io/badge/geopy-2.3.0-ff0066)](https://pypi.org/project/geopy/) [![numpy](https://img.shields.io/badge/numpy-1.24.3-cc00ff)](https://pypi.org/project/numpy/) [![pandas](https://img.shields.io/badge/pandas-2.0.2-ffff00)](https://pypi.org/project/pandas/) [![python-dateutil](https://img.shields.io/badge/python--dateutil-2.8.2-669900)](https://pypi.org/project/python-dateutil/) [![pytz](https://img.shields.io/badge/pytz-2023.3-660033)](https://pypi.org/project/pytz/) [![six](https://img.shields.io/badge/six-1.16.0-996633)](https://pypi.org/project/six/) [![tzdata](https://img.shields.io/badge/tzdata-2023.3-339933)](https://pypi.org/project/tzdata/)


E2-RideKit is a comprehensive toolkit designed to enhance ridesharing datasets with crucial information related to emissions and equity. It addresses the challenges faced in emission-aware ride assignment algorithms, making it a valuable contribution to the ridesharing research community.

## Motivation

Our work on developing emission-aware ride assignment algorithms necessitated ridesharing datasets to include carbon emission information for deadhead miles and individual trips, along with equity-related metrics on drivers and riders. Since no existing datasets contain such information, the E2-RideKit was developed to augment existing datasets, solving multiple challenges along the way.

## Installation

### For Unix-based Systems/ Windows:

1. Clone the repository:
   ```bash
   git clone https://github.com/mahsahebdel/E2-rideKit.git
   ```

2. Navigate to the toolkit directory:
   ```bash
   cd e2-ridekit
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install the E2-RideKit Python package:
   ```bash
   pip install -e .
   ```

## Data Requirements

E2-RideKit requires the following data inputs:

- Ridesharing Dataset (CSV): Contains information on individual rides, including start and end locations, timestamps, and driver/rider IDs.
- Driver/Rider Dataset (CSV) (Optional): Contains additional information on all drivers and riders if available.

Ensure that your datasets have the required columns for the toolkit to perform the necessary augmentations.

## Functions

E2-RideKit provides various functions to perform calculations and augment datasets:

- `calculate_Deadhead(trips)`: Calculates deadhead miles based on previous drop-off and current pick-up locations.
- `calculate_deadheadEmission(trips)`: Calculates deadhead emissions based on deadhead miles and emission factor.
- `calculate_traveledEmission(trips)`: Calculates emissions during the actual trip based on traveled distance and emission factor.
- `calculate_ev_metrics(trips, ev_percentage, grid_intensity)`: The function randomly selects a percentage (ev_percentage) of unique drivers from the dataset to represent EV drivers. For the selected EV drivers, you can establish the emission equivalent for unit distance, based on location, for Electric Vehicles, using values like 63.35 g.CO2eq/km. This incorporates the average carbon intensity specific to Austin, Texas.. This allows the simulation of emissions adjustments for a proportion of the vehicle fleet transitioning to Electric Vehicles in the context of the provided dataset.

- `filter_trips_by_date(trips, start_date, end_date)`: Filters trips based on a specified date range.
- `get_random_samples(trips, num_samples)`: Retrieves a random sample of trips from the dataset.
- `calculate_Distance(lat1, lon1, lat2, lon2)`: Calculates the great-circle distance between two points.

## Usage

To use E2-RideKit, run the main script with various command-line options. For example:

- `-d`: this option computes deadhead miles, which refers to the distance traveled by a vehicle without passengers.
```bash

e2ridekit_package -d -i input_dataset.csv -o output_dataset.csv
```

- `-de`: calculates deadhead emissions, representing the emissions produced during the travel of a vehicle without passengers.

```bash

e2ridekit_package -de -i input_dataset.csv -o output_dataset.csv
```

- `-t`: calculates traveled distance, encompassing the entire distance covered during rides.

```bash

e2ridekit_package -t -i input_dataset.csv -o output_dataset.csv
```

- `-te`: calculates traveled emissions, considering the distance covered with passengers.

```bash

e2ridekit_package -te -i input_dataset.csv -o output_dataset.csv
```

- `-ev`: adjusts emissions for Electric Vehicles (EVs). This option configures settings for electric vehicles, including the percentage of electric vehicles in the dataset and the location-based grid intensity value.

```bash

e2ridekit_package -ev 20 63.35 -i input_dataset.csv -o output_dataset.csv
```

- `-sd` and `-ed`: specifies the start date and end date respectively for filtering the dataset. Trips before start date and after end date will be excluded from the calculations. 

```bash

e2ridekit_package -i input_dataset.csv -o output_dataset.csv -sd 2016-06-04 -ed 2016-06-06
```

- `-n`: determines the number of random samples to retrieve from the dataset for analysis.

```bash

e2ridekit_package -i input_dataset.csv -o output_dataset.csv -n 10
```


## Dependencies

E2-RideKit has the following dependencies:

- [geographiclib==2.0](https://pypi.org/project/geographiclib/)
- [geopy==2.3.0](https://pypi.org/project/geopy/)
- [numpy==1.24.3](https://pypi.org/project/numpy/)
- [pandas==2.0.2](https://pypi.org/project/pandas/)
- [python-dateutil==2.8.2](https://pypi.org/project/python-dateutil/)
- [pytz==2023.3](https://pypi.org/project/pytz/)
- [six==1.16.0](https://pypi.org/project/six/)
- [tzdata==2023.3](https://pypi.org/project/tzdata/)

## Publication

If you use E2-RideKit in an academic work, please consider citing our paper:  
A Holistic Approach for Equity-aware Carbon Reduction of Ridesharing Platforms; Mahsa Sahebdel, Ali Zeynali, Noman Bashir, Prashant Shenoy, Mohammad Hajiesmaili.
[e-Energy 2024]

## Help and Resources

For assistance or inquiries, you can reach out to Mahsa Sahebdel at msahebdelala@umass.edu. Please be patient as it may take a few hours to a day to respond.

## Acknowledgments

This toolkit is developed as part of our work on emission-aware ride assignment algorithms.

