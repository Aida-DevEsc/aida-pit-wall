import fastf1
from fastf1 import plotting
import matplotlib.pyplot as plt

# 1. setup the f1 look
plotting.setup_mpl(misc_mpl_mods=False)

# 2. get the 2025 British Grand Prix qualifying data
session = fastf1.get_session(2026, 'melbourne', 'Q')
session.load()

# 3. choose your rivals
driver_a = 'NOR'  # Lando Norris
driver_b = 'RUS'  # Lewis Hamilton

# 4. grab their fastest laps
lap_a = session.laps.pick_drivers(driver_a).pick_fastest()
lap_b = session.laps.pick_drivers(driver_b).pick_fastest()

# 5. extract telemetry data
tel_a = lap_a.get_telemetry().add_distance()
tel_b = lap_b.get_telemetry().add_distance()

# 6. create the "engineer's dashboard"
fig, ax = plt.subplots(3, sharex=True, gridspec_kw={'hspace': 0.1}, figsize=(12, 8))

# subplot 1: speed 
ax[0].plot(tel_a['Distance'], tel_a['Speed'], label=driver_a, color='Orange') # mclaren orange
ax[0].plot(tel_b['Distance'], tel_b['Speed'], label=driver_b, color='silver') # mercedes silver
ax[0].set_ylabel('Speed (km/h)')
ax[0].legend(loc='upper right')

# subplot 2: throttle
ax[1].plot(tel_a['Distance'], tel_a['Throttle'], label=driver_a, color='orange')
ax[1].plot(tel_b['Distance'], tel_b['Throttle'], label=driver_b, color='silver')
ax[1].set_ylabel('Throttle (%)')


# subplot 3: brake
ax[2].plot(tel_a['Distance'], tel_a['Brake'], label=driver_a, color='orange')
ax[2].plot(tel_b['Distance'], tel_b['Brake'], label=driver_b, color='silver')
ax[2].set_ylabel('Braking')
ax[2].set_xlabel('Distance (m)')

plt.suptitle(f"The Battle of Melbourne: {driver_a} vs {driver_b}")
plt.show()