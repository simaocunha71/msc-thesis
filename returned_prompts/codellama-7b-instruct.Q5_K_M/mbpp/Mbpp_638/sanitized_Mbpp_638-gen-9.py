def wind_chill(wind_velocity_in_km_h, temperature_in_celsius):
    wind_velocity_in_m_s = wind_velocity_in_km_h / 3.6
    temperature_in_celsius_in_k = temperature_in_celsius + 273.15
    wind_chill_index = (13.12 + (0.6215 * temperature_in_celsius_in_k) - (11.37 * wind_velocity_in_m_s) + (0.3965 * temperature_in_celsius_in_k * wind_velocity_in_m_s) - (0.567 * wind_velocity_in_m_s**2) + (0.2525 * temperature_in_celsius_in_k * wind_velocity_in_m_s**2) + (0.823 * wind_velocity_in_m_s**3) - (0.153 * temperature_in_celsius_in_k * wind_velocity_in_m_s**3) + (0.0165 * wind_velocity_in_m_s**4))
    return round(wind_chill_index)