
def get_total_number_of_sequences(m, n):
  # Write your code here
  total = 0
  for i in range(n):
    total += (m - i) * (m - i + 1) // 2
  return total


