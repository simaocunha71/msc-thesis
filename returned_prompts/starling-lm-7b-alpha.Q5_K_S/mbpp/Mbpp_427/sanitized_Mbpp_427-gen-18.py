def change_date_format(date_str):
  return date_str[::-1].split("-")[0] + "-" + date_str[::-1].split("-")[1] + "-" + date_str[::-1].split("-")[2][::-1]