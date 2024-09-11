def perfect_squares(start, end):
    return [i**2 for i in range(int(start**0.5), int(end**0.5)+1) if start <= i**2 <= end]  # or use math.sqrt and math.floor for more precision