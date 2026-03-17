import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv('LV3_Files\data_C02_emission.csv')

data.drop_duplicates()

data['CO2 Emissions (g/km)'].plot(kind='hist', bins = 20)
plt.show()

px.scatter(data, 'CO2 Emissions (g/km)', 'Fuel Consumption City (L/100km)', color="key", color_discrete_sequence=df["colors"].tolist())

plt.show()