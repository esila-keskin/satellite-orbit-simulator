from poliastro.bodies import Earth
from poliastro.twobody import Orbit
from astropy import units as u

# Define a satellite orbiting Earth at 500 km altitude
orbit = Orbit.circular(Earth, alt=500 * u.km)

# Output the orbit details
print("Satellite Orbit:")
print(orbit)
