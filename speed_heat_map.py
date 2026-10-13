import fastf1
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

# 1. Load the session
session = fastf1.get_session(2026, 'melbourne', 'Q')
session.load()

# 2. Pick a driver and their fastest lap Hamilton (HAM) 
lap = session.laps.pick_drivers('RUS').pick_fastest()
tel = lap.get_telemetry()

# 3. get x, y, and speed
x = tel['X']
y = tel['Y']
color = tel['Speed']

# 4. Create "segments" to color the line 
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# 5. build the plot
fig, ax = plt.subplots(sharex=True, sharey=True, figsize=(12, 6.75))
fig.suptitle(f"Speed Heat Map: Russels 2026 melbourne Qualifying", size=24, y=0.97)

# 6. create the colored line 
norm = plt.Normalize(color.min(), color.max())
lc = LineCollection(segments, cmap='magma', norm=norm, linestyle='-', linewidth=5)
lc.set_array(color)

# add the line collection to the plot
line = ax.add_collection(lc)
ax.autoscale()

# 6. clean up the "map" 
plt.colorbar(line, label='Speed (km/h)')
ax.axis('off') # hide axes for a cleaner look
plt.show()
