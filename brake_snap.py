import fastf1
from fastf1 import plotting
import matplotlib.pyplot as plt

plotting.setup_mpl(misc_mpl_mods=False)

# 1. Load Monaco qualifying 
session = fastf1.get_session(2024, 'monaco', 'Q')
session.load()

# 2. Choose your rivals
lec = session.laps.pick_driver('LEC').pick_fastest()
pia = session.laps.pick_driver('PIA').pick_fastest()

tel_lec = lec.get_telemetry().add_distance()
tel_pia = pia.get_telemetry().add_distance()

# 3. Create the "detective" view
fig, ax = plt.subplots(3, sharex=True, figsize=(12, 8))
fig.suptitle("Monaco Qualifying: Charles Leclerc vs OscarPiastri")

# row 1: speed
ax[0].plot(tel_lec['Distance'], tel_lec['Speed'], label='Leclerc', color='red')
ax[0].plot(tel_pia['Distance'], tel_pia['Speed'], label='Piastri', color='orange')
ax[0].set_ylabel('Speed (km/h)')

# row 2: brake
ax[1].plot(tel_lec['Distance'], tel_lec['Brake'], label='Leclerc', color='red')
ax[1].plot(tel_pia['Distance'], tel_pia['Brake'], label='Piastri', color='orange')
ax[1].set_ylabel('Brake (on/off)')

# row 3: throttle
ax[2].plot(tel_lec['Distance'], tel_lec['Throttle'], label='Leclerc', color='red')
ax[2].plot(tel_pia['Distance'], tel_pia['Throttle'], label='Piastri', color='orange')
ax[2].set_ylabel('Throttle (%)')

# 4. ZOOM IN on the hairpin
plt.xlim(600, 900)  
plt.xlabel('Distance (m)')
plt.show()