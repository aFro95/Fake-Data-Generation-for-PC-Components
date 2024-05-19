from faker import Faker
import random
import pandas as pd
import csv
import statistics
import matplotlib.pyplot as plt
import seaborn as sns

fake = Faker()

# Adding lists of manufacturers for each component category
processor_manufacturers = ['Intel', 'AMD']
motherboard_manufacturers = ['ASRock', 'Asus', 'Biostar', 'Gigabyte', 'MSI']
ram_manufacturers = ['ADATA', 'Corsair', 'Crucial', 'G.Skill', 'HyperX', 'Kingston', 'Patriot']
storage_manufacturers = ['ADATA', 'Corsair', 'Crucial', 'Samsung', 'Seagate', 'Western Digital']
video_card_manufacturers = ['Asus', 'Gigabyte', 'MSI', 'Palit', 'Zotac']
power_supply_manufacturers = ['AQIRYS', 'be quiet!', 'Corsair', 'Cooler Master', 'GIGABYTE', 'Seasonic', 'Thermaltake']

def generate_processor_data(num_components):
    # Initialize an empty list to contain the specifications of processors
    specs = []
    
    # For each processor we want to generate
    for _ in range(num_components):
        # Generate specifications for a single processor
        spec = {
            # Randomly choose a manufacturer from the provided list of manufacturers
            'Manufacturer': random.choice(processor_manufacturers), 
            # Generate a fake model name using Faker and capitalize the first letter
            ' Model': fake.word().capitalize(), 
            # Randomly choose the number of cores from a predefined list
            ' Cores': random.choice([4, 6, 8, 12, 16, 24]), 
            # Generate a random frequency between 2.0 and 5.0 GHz and round it to 2 decimal places
            ' Frequency (GHz)': f"{round(random.uniform(2.0, 5.0), 2)} GHz",
            # Generate a random price between 400 and 3000 RON and round it to 2 decimal places
            ' Price': f"{round(random.uniform(400, 3000), 2)} RON"
        }
        # Add the processor specifications to the list of specifications
        specs.append(spec)
    
    # Create a Pandas DataFrame from the list of specifications and return it
    return pd.DataFrame(specs)

def generate_motherboard_data(num_components, processor_type):
    # Check the processor type and define the available choices for motherboard socket and chipset
    if processor_type == 'Intel':
        socket_choices = ['LGA1151 v2', 'LGA1200', 'LGA1700', 'LGA2066']
        chipset_choices = ['B250', 'B460', 'B560', 'B550', 'B760', 'H310', 'H410', 'H470', 'H510', 'H610', 'Z390', 'Z490', 'Z590', 'Z690', 'Z790']
    elif processor_type == 'AMD':
        socket_choices = ['AM4', 'AM5']
        chipset_choices = ['A320', 'A520', 'A620', 'B350', 'B450', 'B550', 'B650', 'X470', 'X570', 'X670']
    else:
        raise ValueError("Invalid processor type")
        
    # Generate specifications for motherboards using the available choices for socket and chipset
    specs = [{'Manufacturer': random.choice(motherboard_manufacturers), 
              ' Model': fake.word().capitalize(),
              ' Form Factor': random.choice(['ATX', 'eATX', 'mATX', 'mITX']), 
              ' Processor Socket': random.choice(socket_choices), 
              ' Chipset': random.choice(chipset_choices),
              ' Price': f"{round(random.uniform(300, 2000), 2)} RON"}
              for _ in range(num_components)]
              
    # Return a Pandas DataFrame created from the generated specifications
    return pd.DataFrame(specs)

def generate_ram_data(num_components):
    # Initialize an empty list to store the specifications of the generated RAM modules
    specs = []
    # Iterate to generate specifications for each RAM component
    for _ in range(num_components):
        # Randomly choose a RAM speed from a predefined list of values
        speed = random.choice([2133, 2400, 2666, 3000, 3200, 3600, 5200, 5600, 6000])
        # Add the specifications for the current RAM component to the specs list
        specs.append({
            'Manufacturer': random.choice(ram_manufacturers),  # Randomly choose a manufacturer from the list of RAM manufacturers
            ' Model': fake.word().capitalize(),  # Generate a random fake name for the RAM model
            ' Capacity (GB)': f"{random.choice([4, 8, 16, 32, 64])} GB",  # Randomly choose the RAM capacity
            ' Speed (MHz)': f"{speed} MHz",  # Use the randomly generated speed
            ' Type': 'DDR5' if speed > 3600 else 'DDR4',  # Determine the type of RAM (DDR4 or DDR5) based on speed
            ' Price': f"{round(random.uniform(80, 1500), 2)} RON"  # Generate a random price for the RAM component
        })
    # Return a Pandas DataFrame created from the generated specifications
    return pd.DataFrame(specs)

def generate_hdd_data(num_components):
    # Initialize an empty list to store the specifications of the generated hard disks
    specs = []
    # Iterate to generate specifications for each hard disk
    for _ in range(num_components):
        # Add the specifications for the current hard disk to the specs list
        specs.append({
            'Manufacturer': random.choice(storage_manufacturers),  # Randomly choose a manufacturer from the list of storage manufacturers
            ' Model': fake.word().capitalize(),  # Generate a random fake name for the hard disk model
            ' Capacity_TB': f"{random.choice([1, 2, 3, 4, 5, 6, 8, 10])} TB",  # Randomly choose the hard disk capacity
            ' Speed (RPM)': f"{random.choice([5400, 7200])} RPM",  # Randomly choose the hard disk rotation speed
            ' Price': f"{round(random.uniform(200, 1000), 2)} RON"  # Generate a random price for the hard disk
        })
    # Return a Pandas DataFrame created from the generated specifications
    return pd.DataFrame(specs)

def generate_ssd_data(num_components):
    # Initialize an empty list to store the specifications of the generated SSDs
    specs = []
    # Iterate to generate specifications for each SSD
    for _ in range(num_components):
        # Add the specifications for the current SSD to the specs list
        specs.append({
            'Manufacturer': random.choice(storage_manufacturers),  # Randomly choose a manufacturer from the list of storage manufacturers
            ' Model': fake.word().capitalize(),  # Generate a random fake name for the SSD model
            ' Capacity_GB': f"{random.choice([120, 128, 240, 256, 500, 512, 1000, 2000])} GB",  # Randomly choose the SSD capacity
            ' Write Speed (MB/s)': f"{random.choice(['Between 1500 - 2000', 'Between 1500 - 2000', 'Between 2000 - 2500', 'Between 2500 - 3000', 'Between 3000 - 4000', 'Over 5000'])} MB/s",
            ' Read Speed (MB/s)': f"{random.choice(['Between 1500 - 2000', 'Between 1500 - 2000', 'Between 2000 - 2500', 'Between 2500 - 3000', 'Between 3000 - 4000', 'Over 5000'])} MB/s",
            ' Price': f"{round(random.uniform(70, 1500), 2)} RON" 
        })
    # Return a Pandas DataFrame created from the generated specifications
    return pd.DataFrame(specs)

def generate_powersupply_data(num_components):
    # Available certification options for power supplies
    certification_choices = ['80 Plus Bronze', '80 Plus Silver', '80 Plus Gold', '80 Plus Platinum', '80 Plus Titanium']
    # Generate specifications for power supplies
    specs = [{'Manufacturer': random.choice(power_supply_manufacturers),
              ' Model': fake.word().capitalize(),  # Generate a random fake name for the power supply model
              ' Power (W)': f"{random.choice([500, 550, 600, 650, 750, 850, 1000, 1200, 1500, 2000])} W", 
              ' Certification': random.choice(certification_choices),  # Randomly choose the certification of the power supply from the available options
              ' Price': f"{round(random.uniform(100, 1000), 2)} RON"} 
              for _ in range(num_components)] 
    # Return a Pandas DataFrame created from the generated specifications
    return pd.DataFrame(specs)

def generate_video_card_data(num_components):
    # Generate specifications for video cards
    specs = [{'Manufacturer': random.choice(video_card_manufacturers),  # Randomly choose a manufacturer from the list of video card manufacturers
              ' Model': f"{fake.word().capitalize()} {random.choice([3300, 3400, 3500, 3600, 3700, 3800, 3900, 
                                                                     4000, 4100, 4200, 4300, 4400, 4500, 4600, 
                                                                     4700, 4800, 4900, 5000, 5100, 5200, 5300, 
                                                                     5400, 5500])}",  # Generate a random fake name for the video card model, combined with a random number
              ' Memory (GB)': f"{random.choice([4, 6, 8, 12, 16, 24])} GB",  # Randomly choose the amount of memory for the video card
              ' Memory BUS (bit)': f"{random.choice([128, 192, 256])} bit",  # Randomly choose the memory bus width of the video card
              ' Price': f"{round(random.uniform(1000, 10000), 2)} RON"}  # Generate a random price for the video card
              for _ in range(num_components)]  # For each component, generate the specifications of the video card
    # Return a Pandas DataFrame created from the generated specifications
    return pd.DataFrame(specs)

processor_data = generate_processor_data(1000)
processor_data.to_csv('./CSV/processor_data.csv', index=False)

# Generating data for motherboards for Intel processors
motherboard_data_intel = generate_motherboard_data(1000, 'Intel')

# Generating data for motherboards for AMD processors
motherboard_data_amd = generate_motherboard_data(1000, 'AMD')

# Concatenating the data for Intel and AMD processors into a single DataFrame
motherboard_data = pd.concat([motherboard_data_intel, motherboard_data_amd], ignore_index=True)

# Saving the data to a CSV file
motherboard_data.to_csv('./CSV/motherboard_data.csv', index=False)

ram_data = generate_ram_data(1000)
ram_data.to_csv('./CSV/ram_data.csv', index=False)

hdd_data = generate_hdd_data(1000)
hdd_data.to_csv('./CSV/hdd_data.csv', index=False)

ssd_data = generate_ssd_data(1000)
ssd_data.to_csv('./CSV/ssd_data.csv', index=False)

powersupply_data = generate_powersupply_data(1000)
powersupply_data.to_csv('./CSV/powersupply_data.csv', index=False)

videocard_data = generate_video_card_data(1000)
videocard_data.to_csv('./CSV/videocard_data.csv', index=False)

def read_csv_and_get_prices(processor_data):
    # Open the CSV file with processor data
    with open(processor_data, newline='', encoding='utf-8') as csvfile:
        # Create a reader for the CSV file using the csv module
        reader = csv.DictReader(csvfile)
        # Extract the prices from each row of the CSV file, then replace the word "RON" with an empty string to get only the numeric value of the price, and save them in a list
        prices = [float(row[' Price'].replace('RON', '')) for row in reader]
    # Return the list of prices
    return prices

# Calling the function to get the prices of processors from the CSV file
processor_prices = read_csv_and_get_prices('./CSV/processor_data.csv')

# Calculating the average price of processors
average_processor_price = statistics.mean(processor_prices)
# Finding the minimum price of processors
minimum_processor_price = min(processor_prices)
# Finding the maximum price of processors
maximum_processor_price = max(processor_prices)

# Displaying the results
print(f"The average price of processors is: {average_processor_price:.2f} RON")
print(f"The minimum price of processors is: {minimum_processor_price:.2f} RON")
print(f"The maximum price of processors is: {maximum_processor_price:.2f} RON")

def read_csv_and_get_prices(motherboard_data):
    # Open the CSV file with motherboard data
    with open(motherboard_data, newline='', encoding='utf-8') as csvfile:
        # Create a reader for the CSV file using the csv module
        reader = csv.DictReader(csvfile)
        # Extract the prices from each row of the CSV file, then replace the word "RON" with an empty string to get only the numeric value of the price, and save them in a list
        prices = [float(row[' Price'].replace('RON', '')) for row in reader]
    # Return the list of prices
    return prices

# Calling the function to get the prices of processors from the CSV file
motherboard_prices = read_csv_and_get_prices('./CSV/motherboard_data.csv')

# Calculating the average price of processors
average_motherboard_price = statistics.mean(motherboard_prices)
# Finding the minimum price of motherboards
minimum_motherboard_price = min(motherboard_prices)
# Finding the maximum price of motherboards
maximum_motherboard_price = max(motherboard_prices)

# Displaying the results
print(f"The average price of motherboards is: {average_motherboard_price:.2f} RON")
print(f"The minimum price of motherboards is: {minimum_motherboard_price:.2f} RON")
print(f"The maximum price of motherboards is: {maximum_motherboard_price:.2f} RON")

def read_csv_and_get_prices(ram_data):
    # Read the CSV file and extract the prices and manufacturers into separate lists
    prices = []
    manufacturers = []
    with open(ram_data, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            prices.append(float(row[' Price'].replace(' RON', '')))
            manufacturers.append(row['Manufacturer'])
    return prices, manufacturers

# Get the prices and manufacturers from the RAM CSV file
ram_prices, ram_manufacturers = read_csv_and_get_prices('./CSV/ram_data.csv')

# Build a DataFrame for RAM prices and manufacturers
ram_data = pd.DataFrame({'Manufacturer': ram_manufacturers, ' Price': ram_prices})

# Calculate the maximum and minimum prices for each manufacturer
max_price_by_manufacturer = ram_data.groupby('Manufacturer').max()
min_price_by_manufacturer = ram_data.groupby('Manufacturer').min()

# Get the manufacturers with the highest and lowest prices
most_expensive_manufacturer = max_price_by_manufacturer[' Price'].idxmax()
most_expensive_price = max_price_by_manufacturer[' Price'].max()
least_expensive_manufacturer = min_price_by_manufacturer[' Price'].idxmin()
least_expensive_price = min_price_by_manufacturer[' Price'].min()

# Display the results
print("Manufacturer with the most expensive RAM:", most_expensive_manufacturer, "-", most_expensive_price, "RON")
print("Manufacturer with the cheapest RAM:", least_expensive_manufacturer, "-", least_expensive_price, "RON")

def read_csv_and_get_capacity(hdd_data):
    # Open the CSV file with HDD data
    with open(hdd_data, newline='', encoding='utf-8') as csvfile:
        # Create a reader for the CSV file using the csv module
        reader = csv.DictReader(csvfile)
        # Extract the capacities from each row of the CSV file, remove the units, and save them in a list
        capacities = [float(row[' Capacity_TB'].split()[0]) for row in reader]
    # Return the list of capacities
    return capacities

# Call the function to get the capacities of HDDs from the CSV file
hdd_capacities = read_csv_and_get_capacity('./CSV/hdd_data.csv')

# Calculate the average capacity of HDDs
average_hdd_capacity = statistics.mean(hdd_capacities)

# Display the result
print(f"The average capacity of HDDs is: {average_hdd_capacity:.2f} TB")

# Function to extract numeric prices from a list containing currencies ("RON")
def extract_prices(prices):
    return [float(price.replace(' RON', '')) for price in prices]

# Read SSD data from the CSV file
ssd_data = pd.read_csv('./CSV/ssd_data.csv')

# Extract SSD prices
ssd_prices = extract_prices(ssd_data[' Price'])

# Calculate statistics
mean_ssd_price = statistics.mean(ssd_prices)
median_ssd_price = statistics.median(ssd_prices)

# Try to find the mode, handling cases where there is no mode or multiple modes
try:
    mode_ssd_price = statistics.mode(ssd_prices)
except statistics.StatisticsError:
    mode_ssd_price = "No mode"

std_deviation_ssd_price = statistics.stdev(ssd_prices)

# Display the results
print(f"The mean price of SSDs is: {mean_ssd_price:.2f} RON")
print(f"The median price of SSDs is: {median_ssd_price:.2f} RON")
print(f"The mode price of SSDs is: {mode_ssd_price}")
print(f"The standard deviation of SSD prices is: {std_deviation_ssd_price:.2f} RON")

def calculate_summary_statistics(dataframe):
    summary_stats = {
        'Average Price (RON)': round(dataframe[' Price'].str.replace(' RON', '').astype(float).mean(), 2),
        'Minimum Price (RON)': round(dataframe[' Price'].str.replace(' RON', '').astype(float).min(), 2),
        'Maximum Price (RON)': round(dataframe[' Price'].str.replace(' RON', '').astype(float).max(), 2),
        'Average Power (W)': round(dataframe[' Power (W)'].str.replace(' W', '').astype(int).mean(), 2),
        'Minimum Power (W)': round(dataframe[' Power (W)'].str.replace(' W', '').astype(int).min(), 2),
        'Maximum Power (W)': round(dataframe[' Power (W)'].str.replace(' W', '').astype(int).max(), 2)
    }
    return summary_stats

# Calculate summary statistics
summary_statistics = calculate_summary_statistics(powersupply_data)

# Print summary statistics
for stat, value in summary_statistics.items():
    print(f"{stat}: {value}")

def calculate_extended_statistics_video_cards(dataframe):
    # Calculate price statistics
    price_series = dataframe[' Price'].str.replace(' RON', '').astype(float)
    memory_series = dataframe[' Memory (GB)'].str.replace(' GB', '').astype(int)
    memory_bus_series = dataframe[' Memory BUS (bit)'].str.replace(' bit', '').astype(int)

    extended_stats = {
        'Average Price (RON)': round(price_series.mean(), 2),
        'Minimum Price (RON)': round(price_series.min(), 2),
        'Maximum Price (RON)': round(price_series.max(), 2),
        'Average Memory (GB)': round(memory_series.mean(), 2),
        'Minimum Memory (GB)': round(memory_series.min(), 2),
        'Maximum Memory (GB)': round(memory_series.max(), 2),
        'Average Memory BUS (bit)': round(memory_bus_series.mean(), 2),
        'Minimum Memory BUS (bit)': round(memory_bus_series.min(), 2),
        'Maximum Memory BUS (bit)': round(memory_bus_series.max(), 2),
        'Manufacturer Distribution': dataframe['Manufacturer'].value_counts().to_dict(),
        'Most Common Model': dataframe[' Model'].mode()[0],
        'Number of Unique Models': dataframe[' Model'].nunique(),
        'Memory Distribution (GB)': memory_series.value_counts().to_dict(),
        'Memory BUS Distribution (bit)': memory_bus_series.value_counts().to_dict(),
        'Price Standard Deviation (RON)': round(price_series.std(), 2),
        'Memory Standard Deviation (GB)': round(memory_series.std(), 2),
        'Memory BUS Standard Deviation (bit)': round(memory_bus_series.std(), 2)
    }
    return extended_stats


# Calculate extended summary statistics
extended_statistics_video_cards = calculate_extended_statistics_video_cards(videocard_data)

# Display the extended statistics
for stat, value in extended_statistics_video_cards.items():
    print(f"{stat}: {value}")