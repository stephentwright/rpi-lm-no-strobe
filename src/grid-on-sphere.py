import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to project points from the tangent plane to the sphere
def project_to_sphere(x, y, z):
    norm = np.sqrt(x**2 + y**2 + z**2)
    return x / norm, y / norm, z / norm

# Grid parameters
s = 0.3  # Side length of the squares in the grid
offsets = [-s, 0, s]

# Generate grid points on the tangent plane
grid_points = [(x, y, 1) for x in offsets for y in offsets]

# Project grid points onto the sphere
sphere_pattern01 = [project_to_sphere(x, y, 1) for x, y, _ in grid_points]
sphere_pattern02 = [project_to_sphere(x, y, -1) for x, y, _ in grid_points]

#TODO: we need to subset sphere_pattern01 to only keep the required dots of pattern 01 from the RPT ball 
# for each pattern (6x) we need to standardise position and map to a vector (1, 3, 5, 7). We keep these
# positions as it will map the dots to the sphere and create a virtual rapsodo ball.
test = [sphere_pattern01[i] for i in [0,3,5]] 
print(test)

# Extract x, y, z components for plotting
#sphere_x, sphere_y, sphere_z = zip(*sphere_pattern01)
sphere_x, sphere_y, sphere_z = zip(*test)
sphere_x2, sphere_y2, sphere_z2 = zip(*sphere_pattern02)

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the unit sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z, color='lightblue', alpha=0.5, rstride=5, cstride=5)

# Plot the original tangent plane grid points
grid_x, grid_y, grid_z = zip(*grid_points)
#ax.scatter(grid_x, grid_y, grid_z, color='red', label="Grid Points (Tangent Plane)")

# Plot the projected points on the sphere
#ax.scatter([sphere_x,sphere_x2], [sphere_y,sphere_y2], [sphere_z,sphere_z2], color='blue', label="Projected Points (Sphere)")
ax.scatter(sphere_x, sphere_y, sphere_z, color='blue', label="Projected Points (Sphere)")
ax.scatter(sphere_x2, sphere_y2, sphere_z2, color='blue', label="Projected Points (Sphere)")

# Labels and legend
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Projection of Tangent Plane Grid onto Unit Sphere")
ax.legend()

plt.show()
