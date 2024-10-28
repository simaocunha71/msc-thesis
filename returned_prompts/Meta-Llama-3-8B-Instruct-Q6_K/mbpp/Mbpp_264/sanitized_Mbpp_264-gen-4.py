def dog_age(years):
  dog_years = 0
  for i in range(years):
    if i < 2:
      dog_years += 15
    else:
      dog_years += 10
  return dog_years