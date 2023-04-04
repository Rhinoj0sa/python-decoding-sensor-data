# Runner script for all modules
from load_data import load_sensor_data, load_sensor_data_with_pandas

##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print("Sensor Data App")
##############################

# Module 1 code here:
data = load_sensor_data()
total_records = 0
for sensor in data:
    # print(f"Loaded {len(data[sensor])} records from {sensor}.")
    total_records += len(data[sensor])
print(f"Loaded records: {total_records} ")


# Module 2 code here:

# Module 3 code here:

# Module 4 code here:

# Module 5 code here:
