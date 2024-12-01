import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def new_position_on_sphere(initial_theta, initial_phi, angular_displacement, direction_angle):
    """
    Calculate the new position on a unit sphere.
    
    Parameters:
        initial_theta (float): Initial polar angle (radians).
        initial_phi (float): Initial azimuthal angle (radians).
        angular_displacement (float): Angular distance moved (radians).
        direction_angle (float): Direction of movement in azimuthal plane (radians).
    
    Returns:
        tuple: New coordinates (x, y, z) on the unit sphere.
    """
    # Update the polar and azimuthal angles
    new_theta = angular_displacement  # Moving from the pole towards the equator
    new_phi = direction_angle
    
    # Calculate the Cartesian coordinates
    x = math.sin(new_theta) * math.cos(new_phi)
    y = math.sin(new_theta) * math.sin(new_phi)
    z = math.cos(new_theta)
    
    return x, y, z

# Inputs
initial_theta = 0  # Starting at the North pole
initial_phi = 0  # Azimuthal angle (irrelevant for the North pole)
angular_displacement = 0.2  # Angular distance moved (radians)
direction_angle = math.pi / 4  # 45 degrees in radians

# Compute new position
new_point1 = new_position_on_sphere(initial_theta, initial_phi, angular_displacement, direction_angle)
new_point2= new_position_on_sphere(initial_theta, initial_phi, angular_displacement, direction_angle*3)
new_point3 = new_position_on_sphere(initial_theta, initial_phi, angular_displacement, direction_angle*4)

# Define sphere parameters for plotting
u = np.linspace(0, 2 * np.pi, 100)  # Azimuthal angle
v = np.linspace(0, np.pi, 100)      # Polar angle

# Sphere coordinates
x_sphere = np.outer(np.cos(u), np.sin(v))
y_sphere = np.outer(np.sin(u), np.sin(v))
z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))

# Plotting
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the sphere
ax.plot_surface(x_sphere, y_sphere, z_sphere, color='cyan', alpha=0.3, edgecolor='gray')

# Plot the initial point (North pole)
ax.scatter(0, 0, 1, color='red', s=100, label="Initial Point (0, 0, 1)")

# Plot the new point
ax.scatter(*new_point1, color='blue', s=100, label="New Point")
ax.scatter(*new_point2, color='green', s=100, label="New Point")
ax.scatter(*new_point3, color='black', s=100, label="New Point")

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Movement on a Unit Sphere')
ax.legend()

plt.show()
