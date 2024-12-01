import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the number of segments
latitude_segments = 19
longitude_segments = 12

# Generate the sphere
phi = np.linspace(0, np.pi, latitude_segments + 1)  # Latitude: 0 to π
theta = np.linspace(0, 2 * np.pi, longitude_segments, endpoint=False)  # Longitude: 0 to 2π

# Create a meshgrid for spherical coordinates
phi, theta = np.meshgrid(phi, theta)

# Convert spherical to Cartesian coordinates
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)

# Plot the sphere
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, rstride=1, cstride=1, color='b', alpha=0.6, edgecolor='k')

# Labels and aspect ratio
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio

plt.title("Unit Sphere with 12 Latitude and 19 Longitude Segments")
plt.show()
