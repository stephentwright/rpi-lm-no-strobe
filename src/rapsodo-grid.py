import matplotlib.pyplot as plt

# Define circle centers and radii
circle_centers = [(5, 3), (6, 1), (6, 2), (7, 3),
                  (5, 7), (6, 6), (7, 6), (7, 7), (6,8),
                  (1, 8.6), (1.8, 9.33), (2.5, 10), (1, 11.4), (1.8,10.66),
                  (5, 11), (7, 11), (6, 12), (7, 13),
                  (11, 8.6), (10.2, 9.2), (11,10), (10.2, 10.8), (11, 11.6),
                  (5, 16), (6, 16), (7, 16), (6, 18)]
circle_radius = 0.25  # Radius for all circles

# Set up the plot
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='datalim')

# Draw each circle
for center in circle_centers:
    circle = plt.Circle(center, circle_radius, edgecolor='blue', fill=True)
    ax.add_patch(circle)

# Set grid limits and enable grid
x_coords, y_coords = zip(*circle_centers)
ax.set_xlim(0, 12)
ax.set_ylim(0, 19)
plt.grid(True)

# Show the plot
# plt.title("Circles on a Grid")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
plt.show()
