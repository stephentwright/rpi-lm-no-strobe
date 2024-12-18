import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define start and end points
start = np.array([0, 0, 1])
end = np.array([0, 1, 1])

# Normalize the end point to lie on the sphere
end = end / np.linalg.norm(end)

# SLERP function
def slerp(p0, p1, t):
    """Spherical linear interpolation between p0 and p1."""
    dot = np.dot(p0, p1)
    dot = np.clip(dot, -1.0, 1.0)  # Ensure numerical stability
    theta = np.arccos(dot)  # Angle between p0 and p1
    sin_theta = np.sin(theta)
    
    if sin_theta < 1e-6:  # If the points are too close
        return (1 - t) * p0 + t * p1  # Linear interpolation fallback
    
    a = np.sin((1 - t) * theta) / sin_theta
    b = np.sin(t * theta) / sin_theta
    return a * p0 + b * p1

# Interpolate points (3 steps)
steps = 3
t_values = np.linspace(0, 1, steps)
path = np.array([slerp(start, end, t) for t in t_values])

# Create figure with subplots
fig = plt.figure(figsize=(10, 5))

# 3D plot of points on the sphere
ax3d = fig.add_subplot(121, projection='3d')
ax3d.set_xlim([-1, 1])
ax3d.set_ylim([-1, 1])
ax3d.set_zlim([-1, 1])
ax3d.set_xlabel("X")
ax3d.set_ylabel("Y")
ax3d.set_zlabel("Z")

# Plot the sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones_like(u), np.cos(v))
ax3d.plot_surface(x, y, z, color='lightblue', alpha=0.5)

# Plot the interpolated points on the sphere
ax3d.scatter(path[:, 0], path[:, 1], path[:, 2], color='red', s=50, label='Interpolated Points')
ax3d.legend()

# 2D projection on the xy-plane
ax2d = fig.add_subplot(122)
ax2d.set_xlim([-1, 1])
ax2d.set_ylim([-1, 1])
ax2d.set_xlabel("X")
ax2d.set_ylabel("Y")
ax2d.set_title("XY Projection")

# Plot the sphere outline in the xy-plane
circle = plt.Circle((0, 0), 1, color='lightblue', fill=False, linewidth=1.5)
ax2d.add_artist(circle)

# Plot the interpolated points on the xy-plane
ax2d.scatter(path[:, 0], path[:, 1], color='red', s=50, label='Interpolated Points')
ax2d.axhline(0, color='gray', linestyle='--', linewidth=0.5)
ax2d.axvline(0, color='gray', linestyle='--', linewidth=0.5)
ax2d.legend()

# Show the plots
plt.tight_layout()
plt.show()
