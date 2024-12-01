import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a sphere
phi, theta = np.mgrid[0:np.pi:180j, 0:2 * np.pi:360j]
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)

# Add dimples (sinusoidal pattern)
dimple_pattern = 0.97 + 0.03 * np.sin(25 * phi) * np.sin(25 * theta)
x_dimpled = x * dimple_pattern
y_dimpled = y * dimple_pattern
z_dimpled = z * dimple_pattern

# Plot the sphere
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d', aspect='auto')
ax.plot_surface(x_dimpled, y_dimpled, z_dimpled, color='white', edgecolor='gray', linewidth=0.1, alpha=0.9)

# Add an 'X' on the equator
x_x = [0.9, -0.9]
y_x = [0.9, -0.9]
z_x = [0, 0]
ax.plot(x_x, y_x, z_x, color='red', linewidth=2, label='X Marker')
ax.plot([-0.9, 0.9], [0.9, -0.9], [0, 0], color='red', linewidth=2)

# Add a marker at the north pole (ChatGPT logo simulation)
# The north pole of the sphere is (0, 0, 1)
ax.text(0, 0, 1.01, "ChatGPT", color='green', fontsize=10, ha='center', va='center', weight='bold')

# Styling
ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio
ax.set_title("3D Golf Ball with X Marker and ChatGPT Logo")
ax.set_axis_off()

plt.show()
