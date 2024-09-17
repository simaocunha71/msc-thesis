def wind_chill(v: int, t: int) -> int:
  return round(13.12 + 0.6215 * t - 11.37 * (v ** 0.16) + 0.3965 * t * (v ** 0.16))