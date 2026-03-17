import pandas as pd
import numpy as np

data = pd.read_csv('LV3_Files\data_C02_emission.csv')

data.drop_duplicates()

print(len(data))

for col in data.select_dtypes(object):
    data[col] = data[col].astype('category')

print(data.dtypes)
LowestCityFuelConsumption = data.sort_values(by = ['Fuel Consumption City (L/100km)'], ascending=False)
HighestCityFuelConsumption = data.sort_values(by = ['Fuel Consumption City (L/100km)'], ascending=True)
print(LowestCityFuelConsumption.loc[:,['Make', 'Model','Fuel Consumption City (L/100km)']].head(3))
print(HighestCityFuelConsumption.loc[:,['Make', 'Model','Fuel Consumption City (L/100km)']].head(3))

certainEngines = data[(data['Engine Size (L)'] <= 3.5) & (data['Engine Size (L)'] >= 2.5)]
print("Number of vehicles with engine size between 2.5 and 3.5:", len(certainEngines))
print("Their average CO2 emission:", certainEngines.loc[:,['CO2 Emissions (g/km)']].mean())

print(len(data[data['Make'] == 'Audi']))

AudiFourCylinder = data[(data['Make'] == 'Audi') & (data['Cylinders'] == 4)]
print("Average CO2 emission in a 4 cylinder Audi:", AudiFourCylinder.loc[:,['CO2 Emissions (g/km)']].mean())

FourCylinderedVehicles = data[(data['Cylinders'] == 4)]
SixCylinderedVehicles = data[(data['Cylinders'] == 6)]
EigthCylinderedVehicles = data[(data['Cylinders'] == 8)]

print("4 cylinders:", FourCylinderedVehicles.loc[:,['CO2 Emissions (g/km)']].mean())
print("6 cylinders:", SixCylinderedVehicles.loc[:,['CO2 Emissions (g/km)']].mean())
print("8 cylinders:", EigthCylinderedVehicles.loc[:,['CO2 Emissions (g/km)']].mean())

DiezelVehicles = data[(data['Fuel Type'] == 'D')]
RegularGasVehicles = data[(data['Fuel Type'] == 'X')]

print("Diezel mean:", DiezelVehicles.loc[:,['CO2 Emissions (g/km)']].mean(), "Diezel median:", DiezelVehicles.loc[:,['CO2 Emissions (g/km)']].median())
print("Regular gas mean:", RegularGasVehicles.loc[:,['CO2 Emissions (g/km)']].mean(), "Regular gas median:", RegularGasVehicles.loc[:,['CO2 Emissions (g/km)']].median())

FourCylinderDiezel = data[(data['Cylinders'] == 4) & (data['Fuel Type'] == 'D')].sort_values(by = ['Fuel Consumption City (L/100km)'], ascending=False)
print("Lowesest consuming 4 cylinder diezel:\n", FourCylinderDiezel.head(1))

ManualVehicles = data[(data['Transmission'].str.contains('M'))]
print("Number of manual vehicles",len(ManualVehicles))

