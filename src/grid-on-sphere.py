import numpy as np
import pandas as pd
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
grid_points_z = [(x, y, 1) for x in offsets for y in offsets]
grid_points_y = [(x, 1, z) for x in offsets for z in offsets]
grid_points_x = [(1, y, z) for y in offsets for z in offsets]
print(grid_points_y)

# Project grid points onto the sphere
sphere_pattern01 = [project_to_sphere(x, y, 1) for x, y, _ in grid_points_z]
sphere_pattern02 = [project_to_sphere(x, y, -1) for x, y, _ in grid_points_z]
sphere_pattern03 = [project_to_sphere(x, 1, z) for x, _, z in grid_points_y]
sphere_pattern04 = [project_to_sphere(x, -1, z) for x, _, z in grid_points_y]
sphere_pattern05 = [project_to_sphere(1, y, z) for _, y, z in grid_points_x]
sphere_pattern06 = [project_to_sphere(-1, y, z) for _, y, z in grid_points_x]

#TODO: we need to subset sphere_pattern01 to only keep the required dots of pattern 01 from the RPT ball 
# for each pattern (6x) we need to standardise position and map to a vector (1, 3, 5, 7). We keep these
# positions as it will map the dots to the sphere and create a virtual rapsodo ball.
# Selecting the desired elements (indices 1, 4, and 7 in a zero-based index system)

sub_pattern01 = [sphere_pattern01[i] for i in [0, 3, 5, 6]]
sub_pattern02 = [sphere_pattern02[i] for i in [0, 1, 3, 5, 7]]
sub_pattern03 = [sphere_pattern03[i] for i in [0, 2, 4, 6]]
sub_pattern04 = [sphere_pattern04[i] for i in [2, 3, 4, 8]]
sub_pattern05 = [sphere_pattern05[i] for i in [0, 1, 2, 3, 6]]
sub_pattern06 = [sphere_pattern06[i] for i in [8, 7, 4, 3, 0]]

# Unzipping the selected elements
sphere_x1, sphere_y1, sphere_z1 = zip(*sub_pattern01)
sphere_x2, sphere_y2, sphere_z2 = zip(*sub_pattern02)
sphere_x3, sphere_y3, sphere_z3 = zip(*sub_pattern03)
sphere_x4, sphere_y4, sphere_z4 = zip(*sub_pattern04)
sphere_x5, sphere_y5, sphere_z5 = zip(*sub_pattern05)
sphere_x6, sphere_y6, sphere_z6 = zip(*sub_pattern06)

# Plotting
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111, projection='3d')
ax.set_axis_off()

# Plot the unit sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z, color='lightgray', alpha=0.5, rstride=1, cstride=1)

# Plot the original tangent plane grid points
grid_x, grid_y, grid_z = zip(*grid_points_z)

# Plot the projected points on the sphere
ax.scatter(sphere_x1, sphere_y1, sphere_z1, color='blue', label="Projected Points (Sphere)")
ax.scatter(sphere_x2, sphere_y2, sphere_z2, color='blue', label="Projected Points (Sphere)")
ax.scatter(sphere_x3, sphere_y3, sphere_z3, color='green', label="Projected Points (Sphere)")
ax.scatter(sphere_x4, sphere_y4, sphere_z4, color='green', label="Projected Points (Sphere)")
ax.scatter(sphere_x5, sphere_y5, sphere_z5, color='red', label="Projected Points (Sphere)")
ax.scatter(sphere_x6, sphere_y6, sphere_z6, color='red', label="Projected Points (Sphere)")

plt.show()

rapsodoBall = {"x":[sphere_x1, sphere_x2, sphere_x3, sphere_x4, sphere_x5, sphere_x6],
               "y":[sphere_x1, sphere_y2, sphere_y3, sphere_y4, sphere_y5, sphere_y6],
               "z": [sphere_x1, sphere_z2, sphere_z3, sphere_z4, sphere_z5, sphere_z6]}

df_rapsodoBall = pd.DataFrame(rapsodoBall)
print(df_rapsodoBall)
