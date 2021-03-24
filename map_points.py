import numpy as np
from datapackage import Package
import matplotlib.pyplot as plt
from pyproj import Transformer


package = Package('https://datahub.io/core/airport-codes/datapackage.json')


airports = ['AMS', 'ANR', 'BRU', 'CRL', 'DHR', 'EIN', 'ENS', 'GLZ', 'GRQ', 'KJK', 'LEY', 'LGG', 'LID', 'LUX', 'LWR',
            'MST', 'OBL', 'OST', 'RTM', 'UDE', 'UTC', 'WOE']

coordinates = []
for resource in package.resources:
    if resource.descriptor['datahub']['type'] == 'derived/csv':
        data = np.array(resource.read())
        for airport in airports:
            if (len(data[np.where(data[:, 9] == airport)[0]]) != 0):
                coordinates.append(data[np.where(data[:, 9] == airport)[0]][0])

roosendaal = [None, None, None, None, None, None, None, None, None, 'Roosendaal', None, '4.4653213, 51.535849']
coordinates.append(roosendaal)
coordinates = np.array(coordinates)
data_array = []
for coordinate in coordinates:
    coords = coordinate[11].split(', ')
    longitude = float(coords[0])
    latitude = float(coords[1])

    transformer = Transformer.from_crs("EPSG:4326", "EPSG:23095", always_xy=True)
    x, y = transformer.transform(longitude, latitude)
    data_array.append([coordinate[9], x, y])

data_array = np.array(data_array)

x = data_array[:, 1].astype(float)
y = data_array[:, 2].astype(float)
fig, ax = plt.subplots()
ax.scatter(x, y)

for i, txt in enumerate(data_array[:, 0]):
    ax.annotate(txt, (x[i], y[i]))

plt.show()