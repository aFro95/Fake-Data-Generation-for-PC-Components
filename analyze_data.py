import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from faker import Faker
from generate_data import processor_data, motherboard_data, ram_data, storage_data, videocard_data, powersupply_data

plt.close("all")
# The number of processors offered by each manufacturer
num_intel_processors = processor_data[processor_data['Manufacturer'] == 'Intel'].shape[0]
num_amd_processors = processor_data[processor_data['Manufacturer'] == 'AMD'].shape[0]

# List with the number of processors for each manufacturer
processor_counts = [num_intel_processors, num_amd_processors]

# Labels for each section of the pie chart
labels = ['Intel', 'AMD']

# Custom colors for each section
colors = ['#49FF33', '#FF10ED']

# Creating the pie chart with styling
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(processor_counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, shadow=True)
ax.set_title('Proportion of Processors Offered by Intel vs. AMD', fontsize=16, fontweight='bold', color='blue')
ax.axis('equal')  # Ensures the pie chart is circular

# Adding a custom legend below the chart
ax.legend(title='Manufacturer', loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2, fontsize=12)

# Saving to an image file
plt.savefig('./images/charts/processor_pie_chart.png', bbox_inches='tight')

# Centering the output in the notebook
plt.show()

# Reading data from the CSV file
data = pd.read_csv('./CSV/motherboard_data.csv')

# Removing 'RON' and converting prices to float
data[' Price'] = data[' Price'].str.replace('RON', '').astype(float)

# Calculating the average prices for each chipset
average_prices = data.groupby(' Chipset')[' Price'].mean().reset_index()

# Creating the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(average_prices[' Chipset'], average_prices[' Price'], alpha=0.6, color='darkblue')

# Adding title and axis labels
plt.title('Average Motherboard Prices by Chipset', fontsize=16, color='darkblue')
plt.xlabel('Chipset', fontsize=12)
plt.ylabel('Average Price (RON)', fontsize=12)

# Rotating x-axis labels for readability
plt.xticks(rotation=45)

# Adding a line connecting the points
plt.plot(average_prices[' Chipset'], average_prices[' Price'], linestyle='-', color='red')

plt.savefig('./images/charts/motherboard_scatter_plot_chart.png')

# Displaying the plot
plt.grid(True)
plt.tight_layout()
plt.show()

# Reading data from the CSV file
ram_data = pd.read_csv('./CSV/ram_data.csv')

# Preprocessing data for the Pie Chart regarding capacities
ram_capacity = ram_data[' Capacity (GB)'].value_counts()

# Creating the Pie Chart for capacities
plt.figure(figsize=(8, 8))
colors = ['red', 'green', 'cyan', 'yellow', 'magenta']

plt.pie(ram_capacity, labels=ram_capacity.index, autopct='%1.1f%%', colors=colors)
plt.title('Proportion of RAM Module Capacities', fontsize=16, pad=20)
plt.axis('equal')

# Saving to an image file
plt.savefig('./images/charts/ram_pie_chart.png', bbox_inches='tight')
# Displaying the Pie Chart
plt.show()

# Reading data from the CSV file
hdd_data = pd.read_csv('./CSV/hdd_data.csv')

# Checking the data type for the 'Capacity_TB' column
print(hdd_data[' Capacity_TB'].dtype)

# Ensuring the column name is correct and cleaning the data
# Values might already be numeric, we check and transform if necessary
if hdd_data[' Capacity_TB'].dtype == object:
    hdd_data[' Capacity_TB'] = hdd_data[' Capacity_TB'].str.replace(' TB', '').astype(float)

# Counting the capacities
capacity_counts = hdd_data[' Capacity_TB'].value_counts()

# Creating the bar chart
plt.figure(figsize=(10, 6))
capacity_counts.sort_index().plot(kind='bar', color='skyblue')

plt.title('Number of HDDs by Capacity (TB)')
plt.xlabel('Capacity (TB)')
plt.ylabel('Number of HDDs')
plt.xticks(rotation=0)

plt.savefig('./images/charts/hdd_histogram_chart.png', bbox_inches='tight')

plt.show()

# Read data from CSV file
ssd_data = pd.read_csv('./CSV/ssd_data.csv')

# Clean and transform column ' Capacity (GB)' to numeric type
if ssd_data[' Capacity_GB'].dtype == object:
    ssd_data[' Capacity_GB'] = ssd_data[' Capacity_GB'].str.replace(' GB', '').astype(int)

# Capacity count
capacity_counts = ssd_data[' Capacity_GB'].value_counts()
colors = ['orange', 'purple', 'gray', 'mediumseagreen', 'salmon', 'lime', 'olive', 'teal']
# Create pie chart
plt.figure(figsize=(8, 8))

capacity_counts.plot(kind='pie', autopct='%1.1f%%', colors=colors)
plt.title('Proportion of SSDs by Capacity (GB)')
plt.ylabel('') # Remove y-axis label for pie chart

plt.savefig('./images/charts/ssd_pie_chart.png', bbox_inches='tight')
plt.show()

# Set a more pleasant font for titles and axis labels
plt.rcParams['font.family'] = 'Arial'

plt.figure(figsize=(10, 6))
powersupply_data[' Power (W)'].value_counts().plot(kind='bar', color='skyblue')

# Add gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Modify title font
plt.title('Distribution of Power Supplies by Power (Bar Chart)', fontsize=16, fontweight='bold')

# Modify axis labels font and rotation angle for x-axis labels
plt.xlabel('Power (W)', fontsize=12)
plt.ylabel('Number of Power Supplies', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)  # Align x-axis labels to the right and reduce font size

# Add a shadow to the title bar
plt.title('Distribution of Power Supplies by Power (Bar Chart)', fontsize=16, fontweight='bold', color='blue', pad=20)
plt.savefig('./images/charts/powersupply_bar_chart.png', bbox_inches='tight')

plt.show()

# Setting a custom style using Seaborn
sns.set(style="whitegrid")

# Create histogram for video card memory distribution
plt.figure(figsize=(10, 6))
sns.histplot(data=videocard_data, x=' Memory (GB)', bins=10, kde=True, color='skyblue', alpha=0.7)

# Adding title and axis labels with customized font properties
plt.title('Distribution of Video Card Memory', fontsize=16, fontweight='bold', color='blue')
plt.xlabel('Memory (GB)', fontsize=12, fontweight='bold')
plt.ylabel('Number of Video Cards', fontsize=12, fontweight='bold')

# Adjusting tick labels font size and rotation for better readability
plt.xticks(fontsize=10, rotation=45)
plt.yticks(fontsize=10)

# Adding grid lines
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.savefig('./images/charts/videocard_histogram_chart.png', bbox_inches='tight')

plt.show()

# Generating fake categorical data using Faker
fake = Faker()
categories = [fake.word() for _ in range(10)]

# Creating a count plot using Seaborn
plt.figure(figsize=(10, 6))
sns.countplot(x=categories, hue=categories, palette='pastel', legend=False)
plt.title('Count of Fake Categories')
plt.xlabel('Categories')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()