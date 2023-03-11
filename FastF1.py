# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 23:52:37 2023

@author: Antonio
"""
import fastf1 as f1
import matplotlib.pyplot as plt


session = f1.get_session(2019, 'Monza', 'Q')
session.load(telemetry=False, laps=False, weather=False)
vettel = session.get_driver('VET')
print(f"Pronto {vettel['FirstName']}?")


f1.plotting.setup_mpl()

session = f1.get_session(2019, 'Monza', 'Q')

session.load()
fast_leclerc = session.laps.pick_driver('LEC').pick_fastest()
lec_car_data = fast_leclerc.get_car_data()
t = lec_car_data['Time']
vCar = lec_car_data['Speed']

# The rest is just plotting
plt.plot(t, vCar, label = 'Fast')
plt.xlabel('Time')
plt.ylabel('Speed/ km/h')
plt.title('Lec')
plt.legend(loc = 'best')
plt.show()

fig, ax = plt.subplots()
ax.plot(t, vCar, label='Fast')
ax.set_xlabel('Time')
ax.set_ylabel('Speed [Km/h]')
ax.set_title('Leclerc is')
ax.legend()
plt.show()
