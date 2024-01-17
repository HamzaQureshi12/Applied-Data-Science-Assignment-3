
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the dataset
data_file_path = 'data.csv'
data_df = pd.read_csv(data_file_path, skiprows=4)

# Filter data for Renewable Energy Consumption
renewable_energy_data = data_df[data_df['Indicator Code'] == 'EG.FEC.RNEW.ZS']

# Select the most recent year available for analysis
year = '2021'
renewable_energy_latest = renewable_energy_data[['Country Name', year]].rename(columns={year: 'Renewable Energy Consumption'})

# Load a world map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge the world map with the renewable energy data
world_map_data = world.merge(renewable_energy_latest, left_on='name', right_on='Country Name', how='left')

# Plotting the world map
plt.figure(figsize=(15, 10))
world_map_data.plot(column='Renewable Energy Consumption', cmap='YlGn', legend=True,
                    legend_kwds={'label': "Renewable Energy Consumption (% of Total Energy Consumption)",
                                 'orientation': "horizontal"})
plt.title('Global Renewable Energy Consumption in 2021')
plt.show()
