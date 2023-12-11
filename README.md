
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

## Usage

To use E2-RideKit, run the main script with various command-line options. For example:

- `-d`: this option computes deadhead miles, which refers to the distance traveled by a vehicle without passengers.
```bash

e2ridekit_package -d -i sample_dataset.csv -o output_dataset.csv
```

- `-de`: calculates deadhead emissions, representing the emissions produced during the travel of a vehicle without passengers.

```bash

e2ridekit_package -de -i sample_dataset.csv -o output_dataset.csv
```

- `-t`: calculates trip distance, encompassing the entire distance covered during rides.

```bash

e2ridekit_package -t -i sample_dataset.csv -o output_dataset.csv
```

- `-te`: calculates trip emissions, considering the distance covered with passengers.

```bash

e2ridekit_package -te -i sample_dataset.csv -o output_dataset.csv
```

- `-ev`: adjusts emissions for Electric Vehicles (EVs). To use this option, provide two inputs in order: the EV percentage, indicating the proportion of drivers with electric vehicles, and the grid intensity, a location-based value influencing emissions.

```bash

e2ridekit_package -ev 20 63.35 -i sample_dataset.csv -o output_dataset.csv
```

- `-sd` and `-ed`: specifies the start date and end date respectively for filtering the dataset. Trips before start date and after end date will be excluded from the calculations. 

```bash

e2ridekit_package -i sample_dataset.csv -o output_dataset.csv -sd 2016-06-04 -ed 2016-06-06
```

- `-nd` and `-n`: specifies the number of random drivers to select, and  the number of random samples per selected driver to retrieve. 

```bash

e2ridekit_package -i sample_dataset.csv -o output_dataset.csv -nd 5 -n 10
```

## Functions

E2-RideKit provides various functions to perform calculations and augment datasets:

- `calculate_Deadhead(trips)`: calculates deadhead miles based on previous drop-off and current pick-up locations.
- `calculate_deadheadEmission(trips)`: calculates deadhead emissions based on deadhead miles and emission factor.
- `calculate_traveledEmission(trips)`: calculates emissions during the actual trip based on traveled distance and emission factor.
- `calculate_ev_metrics(trips, ev_percentage, grid_intensity)`: the function facilitates emissions adjustments for Electric Vehicles (EVs). This command allows you to configure settings for electric vehicles, specifying both the percentage of electric vehicles in the dataset (`ev_percentage`) and the location-based grid intensity value. By using this option, the function randomly selects the specified percentage of unique drivers from the dataset to represent EV drivers. For these selected EV drivers, you can define the emission equivalent for unit distance based on location, such as using values like 63.35 g.CO2eq/km. This incorporates the average carbon intensity specific to Austin, Texas, enabling the simulation of emission adjustments for a proportion of the vehicle fleet transitioning to Electric Vehicles within the provided dataset.
- `filter_trips_by_date(trips, start_date, end_date)`: filters trips based on a specified date range.
- `get_random_samples(trips, num_drivers, num_samples_per_driver)`: retrieves a random sample of trips from the dataset. Retrieves a random sample of trips from the dataset. This function takes two parameters: number of random drivers to select from the dataset, and the number of random samples per selected driver to retrieve from the dataset.
- `calculate_Distance(lat1, lon1, lat2, lon2)`: calculates the great-circle distance between two points.


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

The BibTex citation is given below.

@inproceedings{sahebdel2024holistic,
  title={A Holistic Approach for Equity-aware Carbon Reduction of Ridesharing Platforms},
  author={Sahebdel, Mahsa and Zeynali, Ali and Bashir, Noman and Shenoy, Prashant and Hajiesmaili, Mohammad},
  booktitle={Proceedings of the [e-Energy 2024]},
  year={2024}
}


## Help and Resources

For assistance or inquiries, you can reach out to Mahsa Sahebdel at msahebdelala@umass.edu. Please be patient as it may take a few hours to a day to respond.

## Acknowledgments

This toolkit is developed as part of our work on emission-aware ride assignment algorithms.

