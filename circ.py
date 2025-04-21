import matplotlib.pyplot as plt
import numpy as np

# Define circle parameters
radius = 5
center = (0, 0)

# Generate angles from 0 to 2π
theta = np.linspace(0, 2*np.pi, 100)

# Calculate x and y coordinates
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)

# Create the plot
plt.figure(figsize=(6,6))
plt.plot(x, y)

# Set aspect ratio to 'equal' to ensure the circle appears as a circle
plt.gca().set_aspect('equal')

# Show the plot
plt.show()
