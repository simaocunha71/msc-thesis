
def change_date_format(date_string):
  date_list = date_string.split("-")
  return "{}-{}-{}".format(date_list[2], date_list[1], date_list[0])


