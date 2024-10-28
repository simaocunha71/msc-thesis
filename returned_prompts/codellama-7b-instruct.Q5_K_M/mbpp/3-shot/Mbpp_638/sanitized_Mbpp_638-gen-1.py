def wind_chill(wind_velocity: float, temperature: float) -> int:
  return int((35.74 + (0.6215 * wind_velocity) - (35.75 * temperature) + (0.4275 * temperature * wind_velocity)
            + (0.02 * wind_velocity * wind_velocity)) + 0.5)