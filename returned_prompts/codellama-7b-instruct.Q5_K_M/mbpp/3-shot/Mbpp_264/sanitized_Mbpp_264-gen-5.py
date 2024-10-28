def dog_age(age, breed: str) -> int:
  if breed == "Pug":
    return age * 3
  elif breed == "Golden Retriever":
    return age * 5
  elif breed == "Bulldog":
    return age * 2
  else:
    return age