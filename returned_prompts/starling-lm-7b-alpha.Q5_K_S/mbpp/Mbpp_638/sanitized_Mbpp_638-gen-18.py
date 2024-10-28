def wind_chill(velocity: int, temperature: int) -> int:
    def wind_chill_formula(velocity: int, temperature: int) -> float:
        if velocity < 4.79:
            return 13.12 + 0.6215 * temperature - 11.37 * (velocity ** 0.16) + 3.69 * temperature * (velocity ** 0.16)
        else:
            return 10.91 + 0.33 * temperature - 11.37 * (velocity ** 0.16) + 3.69 * temperature * (velocity ** 0.16)
    return int(round(wind_chill_formula(velocity, temperature)))