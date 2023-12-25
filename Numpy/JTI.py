import numpy as np
from math import sqrt

def calculate_jti(semi_major_axis, perihelion_distance, inclination):
  """Calculates the Jupiter Tisserand Invariant (JTI) value of an asteroid.

  Args:
    semi_major_axis: The asteroid's semi-major axis in AU.
    perihelion_distance: The asteroid's perihelion distance in AU.
    inclination: The asteroid's inclination in degrees.

  Returns:
    The asteroid's JTI value.
  """

  jti = (semi_major_axis + (sqrt(perihelion_distance**2 + (1 - inclination**2)) / 1.7))
  return jti

# Calculate the JTI value of the asteroid.
semi_major_axis = 1.407011303
perihelion_distance = 0.808258933
inclination = 6.025981287
jti = calculate_jti(semi_major_axis, perihelion_distance, inclination)

# Print the JTI value.
print(jti)