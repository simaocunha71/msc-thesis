
def check_monthnumb_number(month_number):
  months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
  if month_number in months_with_31_days:
    return True
  return False


