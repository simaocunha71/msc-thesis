
def wind_chill(wind_velocity: int, temperature: int) -> int:
    def wind_chill(velocity, temp):
        return 3.57 + 0.633 * temp - 0.397 * velocity ** 0.16 + 0.006 * velocity ** 0.18 * temp
    return int(round(wind_chill(wind_velocity, temperature)))


