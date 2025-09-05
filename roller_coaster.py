# Calculate velocity of roller coaster at top of loop
# Using Conservation of Energy: v = sqrt(2g(h - 2R))

g = 9.8  # m/s^2
h = 40   # m
R = 10   # m

velocity = (2 * g * (h - 2 * R)) ** 0.5

print(f"The velocity at the top of the loop is: {velocity:.2f} m/s")