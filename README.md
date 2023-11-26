**E2-RideKit**<br>
E2-RideKit is a comprehensive toolkit designed to enhance ridesharing datasets with crucial information related to emissions and equity. It addresses the challenges faced in emission-aware ride assignment algorithms, making it a valuable contribution to the ridesharing research community.

**Motivation**<br>
Our work on developing emission-aware ride assignment algorithms necessitated ridesharing datasets to include carbon emission information for deadhead miles and individual trips, along with equity-related metrics on drivers and riders. Since no existing datasets contain such information, the E2-RideKit was developed to augment existing datasets, solving multiple challenges along the way.

**Installation**<br>
To install E2-RideKit, follow these steps:

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
4. Install the e2_ridekit python package:
   ```bash
   pip install -e .
   ```

**Data Requirements**<br>
E2-RideKit requires the following data inputs:
- Ridesharing Dataset (CSV): Contains information on individual rides, including start and end locations, timestamps, and driver/rider IDs.
- Driver/Rider Dataset (CSV) (Optional): Contains additional information on all drivers and riders if available.

Ensure that your datasets have the required columns for the toolkit to perform the necessary augmentations.


**Functions**<br>
E2-RideKit provides various functions to perform calculations and augment datasets:

- calculate_Deadhead(trips): Calculates deadhead miles based on previous drop-off and current pick-up locations.
- calculate_deadheadEmission(trips): Calculates deadhead emissions based on deadhead miles and emission factor.
- calculate_traveledEmission(trips): Calculates emissions during the actual trip based on traveled distance and emission factor.
- calculate_ev_metrics(trips, ev_percentage, grid_intensity): The function randomly selects a percentage (ev_percentage) of unique drivers from the dataset to represent EV drivers. For these selected EV drivers, the function assigns the provided grid_intensity value, reflecting the emissions associated with electricity usage. This allows the simulation of emissions adjustments for a proportion of the vehicle fleet transitioning to Electric Vehicles in the context of the provided dataset.

- filter_trips_by_date(trips, start_date, end_date): Filters trips based on a specified date range.
- get_random_samples(trips, num_samples): Retrieves a random sample of trips from the dataset.
- calculate_Distance(lat1, lon1, lat2, lon2): Calculates the great-circle distance between two points.


**Usage**<br>
To use E2-RideKit, run the main script with various command-line options. For example:

Calculate deadhead miles
e2ridekit_package -d -i input_dataset.csv -o output_dataset.csv

 Calculate deadhead emissions
e2ridekit_package -de -i input_dataset.csv -o output_dataset.csv

Calculate traveled distance
e2ridekit_package -t -i input_dataset.csv -o output_dataset.csv

 Calculate traveled emissions
e2ridekit_package -te -i input_dataset.csv -o output_dataset.csv

 Adjust emissions for Electric Vehicles (EVs)
e2ridekit_package -ev 20 63.35 -i input_dataset.csv -o output_dataset.csv

Filter trips by date range
e2ridekit_package -i input_dataset.csv -o output_dataset.csv -sd 2016-06-04 -ed 2016-06-06

 Get random samples of trips
e2ridekit_package -i input_dataset.csv -o output_dataset.csv -n 10



**Dependencies**<br>
E2-RideKit has the following dependencies:
geographiclib==2.0
geopy==2.3.0
numpy==1.24.3
pandas==2.0.2
python-dateutil==2.8.2
pytz==2023.3
six==1.16.0
tzdata==2023.3

**Publication**<br>
If you use E2-RideKit in an academic work, please consider citing our paper:
"A Holistic Approach for Equity-aware Carbon Reduction of Ridesharing Platforms"

**Help and Resources**<br>
For assistance or inquiries, you can reach out to Mahsa Sahebdel at msahebdelala@umass.edu. Please be patient as it may take a few hours to a day to respond.


**Acknowledgments**<br>
This toolkit is developed as part of our work on emission-aware ride assignment algorithms.





