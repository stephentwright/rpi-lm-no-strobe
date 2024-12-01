import numpy as np
import plotly.graph_objects as go

#generate a function that gets the orthoginal vectors to 

# Generate spherical coordinates for the unit sphere
phi = np.linspace(0, 2 * np.pi, 100)  # azimuthal angle
theta = np.linspace(0, np.pi, 100)   # polar angle
phi, theta = np.meshgrid(phi, theta)

# Convert spherical coordinates to Cartesian coordinates
x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)

# Define the tangent plane at (0, 0, 1)
# The normal vector to the tangent plane at (0, 0, 1) is [0, 0, 1].
# Therefore, the tangent plane equation is z = 1.

# Define the square vertices centered at (0, 0, 1) in the tangent plane
# We choose two orthogonal vectors in the tangent plane at (0, 0, 1)
# e1 = [1, 0, 0], e2 = [0, 1, 0]
square_center01 = np.array([0, 0, 1])
square_vertices01 = [
    square_center01 + 0.25 * np.array([1, 0, 0]) + 0.25 * np.array([0, 1, 0]),  # Top-right
    square_center01 - 0.25 * np.array([1, 0, 0]) + 0.25 * np.array([0, 1, 0]),  # Top-left
    square_center01 - 0.25 * np.array([1, 0, 0]) - 0.25 * np.array([0, 1, 0]),  # Bottom-left
    square_center01 + 0.25 * np.array([1, 0, 0]) - 0.25 * np.array([0, 1, 0]),  # Bottom-right
]

# Unpack square vertices for plotting
square_x01, square_y01, square_z01 = zip(*square_vertices01)

# Close the square by repeating the first point
square_x01 += (square_x01[0],)
square_y01 += (square_y01[0],)
square_z01 += (square_z01[0],)

# Define the square vertices centered at (1, 0, 0) in the tangent plane
# We choose two orthogonal vectors in the tangent plane at (1, 0, 0)
# e1 = [0, 0, 1], e2 = [0, 1, 0]
square_center02 = np.array([1, 0, 0])
square_vertices02 = [
    square_center02 + 0.25 * np.array([0, 0, 1]) + 0.25 * np.array([0, 1, 0]),  # Top-right
    square_center02 - 0.25 * np.array([0, 0, 1]) + 0.25 * np.array([0, 1, 0]),  # Top-left
    square_center02 - 0.25 * np.array([0, 0, 1]) - 0.25 * np.array([0, 1, 0]),  # Bottom-left
    square_center02 + 0.25 * np.array([0, 0, 1]) - 0.25 * np.array([0, 1, 0]),  # Bottom-right
]

# Unpack square vertices for plotting
square_x02, square_y02, square_z02 = zip(*square_vertices02)

# Close the square by repeating the first point
square_x02 += (square_x02[0],)
square_y02 += (square_y02[0],)
square_z02 += (square_z02[0],)

square_center03 = np.array([-1, 0, 0])
square_vertices03 = [
    square_center03 + 0.25 * np.array([0, 0, -1]) + 0.25 * np.array([0, 1, 0]),  # Top-right
    square_center03 - 0.25 * np.array([0, 0, -1]) + 0.25 * np.array([0, 1, 0]),  # Top-left
    square_center03 - 0.25 * np.array([0, 0, -1]) - 0.25 * np.array([0, 1, 0]),  # Bottom-left
    square_center03 + 0.25 * np.array([0, 0, -1]) - 0.25 * np.array([0, 1, 0]),  # Bottom-right
]

# Unpack square vertices for plotting
square_x03, square_y03, square_z03 = zip(*square_vertices03)

# Close the square by repeating the first point
square_x03 += (square_x03[0],)
square_y03 += (square_y03[0],)
square_z03 += (square_z03[0],)

square_center04 = np.array([0, -1, 0])
square_vertices04 = [
    square_center04 + 0.25 * np.array([0, 0, -1]) + 0.25 * np.array([1, 0, 0]),  # Top-right
    square_center04 - 0.25 * np.array([0, 0, -1]) + 0.25 * np.array([1, 0, 0]),  # Top-left
    square_center04 - 0.25 * np.array([0, 0, -1]) - 0.25 * np.array([1, 0, 0]),  # Bottom-left
    square_center04 + 0.25 * np.array([0, 0, -1]) - 0.25 * np.array([1, 0, 0]),  # Bottom-right
]

# Unpack square vertices for plotting
square_x04, square_y04, square_z04 = zip(*square_vertices04)

# Close the square by repeating the first point
square_x04 += (square_x04[0],)
square_y04 += (square_y04[0],)
square_z04 += (square_z04[0],)

square_center05 = np.array([0, 0, -1])
square_vertices05 = [
    square_center05 + 0.25 * np.array([0, -1, 0]) + 0.25 * np.array([1, 0, 0]),  # Top-right
    square_center05 - 0.25 * np.array([0, -1, 0]) + 0.25 * np.array([1, 0, 0]),  # Top-left
    square_center05 - 0.25 * np.array([0, -1, 0]) - 0.25 * np.array([1, 0, 0]),  # Bottom-left
    square_center05 + 0.25 * np.array([0, -1, 0]) - 0.25 * np.array([1, 0, 0]),  # Bottom-right
]

# Unpack square vertices for plotting
square_x05, square_y05, square_z05 = zip(*square_vertices05)

# Close the square by repeating the first point
square_x05 += (square_x05[0],)
square_y05 += (square_y05[0],)
square_z05 += (square_z05[0],)

square_center06 = np.array([0, 1, 0])
square_vertices06 = [
    square_center06 + 0.25 * np.array([0, 0, 1]) + 0.25 * np.array([1, 0, 0]),  # Top-right
    square_center06 - 0.25 * np.array([0, 0, 1]) + 0.25 * np.array([1, 0, 0]),  # Top-left
    square_center06 - 0.25 * np.array([0, 0, 1]) - 0.25 * np.array([1, 0, 0]),  # Bottom-left
    square_center06 + 0.25 * np.array([0, 0, 1]) - 0.25 * np.array([1, 0, 0]),  # Bottom-right
]

# Unpack square vertices for plotting
square_x06, square_y06, square_z06 = zip(*square_vertices06)

# Close the square by repeating the first point
square_x06 += (square_x06[0],)
square_y06 += (square_y06[0],)
square_z06 += (square_z06[0],)


# Create the interactive 3D plot
fig = go.Figure()

# Add a surface for the unit sphere
fig.add_trace(go.Surface(x=x, y=y, z=z, colorscale='Viridis', opacity=0.7))

# Add the square on the tangent plane
fig.add_trace(go.Scatter3d(
    x=square_x01, y=square_y01, z=square_z01,
    mode='lines',
    line=dict(color='red', width=5),
    name='Tangent Square 01'
))

# Add the square on the tangent plane
fig.add_trace(go.Scatter3d(
    x=square_x02, y=square_y02, z=square_z02,
    mode='lines',
    line=dict(color='blue', width=5),
    name='Tangent Square 02'
))

# Add the square on the tangent plane
fig.add_trace(go.Scatter3d(
    x=square_x03, y=square_y03, z=square_z03,
    mode='lines',
    line=dict(color='blue', width=5),
    name='Tangent Square 03'
))

# Add the square on the tangent plane
fig.add_trace(go.Scatter3d(
    x=square_x04, y=square_y04, z=square_z04,
    mode='lines',
    line=dict(color='blue', width=5),
    name='Tangent Square 04'
))

# Add the square on the tangent plane
fig.add_trace(go.Scatter3d(
    x=square_x05, y=square_y05, z=square_z05,
    mode='lines',
    line=dict(color='blue', width=5),
    name='Tangent Square 05'
))

# Add the square on the tangent plane
fig.add_trace(go.Scatter3d(
    x=square_x06, y=square_y06, z=square_z06,
    mode='lines',
    line=dict(color='blue', width=5),
    name='Tangent Square 06'
))

# Set the aspect ratio to make the sphere and tangent plane look correct
fig.update_layout(scene=dict(aspectmode='data'))

# Show the plot
fig.show()
