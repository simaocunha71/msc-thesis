def division_elements(tup1, tup2):
  # Initialize result
  result = []

  # Iterate over elements in tuples
  for i in range(len(tup1)):
    # Perform division and append result to list
    result.append(tup1[i]/tup2[i])

  # Return result
  return result