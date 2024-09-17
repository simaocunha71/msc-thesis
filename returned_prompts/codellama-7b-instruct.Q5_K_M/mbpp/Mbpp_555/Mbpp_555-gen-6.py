
def difference(n: int) -> int:
  first_n_natural_numbers = [i for i in range(1, n+1)]
  first_n_natural_numbers_sum = sum(first_n_natural_numbers)
  sum_of_cubes_of_first_n_natural_numbers = sum([i**3 for i in first_n_natural_numbers])
  return first_n_natural_numbers_sum - sum_of_cubes_of_first_n_natural_numbers


