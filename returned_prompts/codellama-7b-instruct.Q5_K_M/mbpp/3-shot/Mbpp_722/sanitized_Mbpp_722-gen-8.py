def filter_data(data, height, weight):
  return {name: info for name, info in data.items() if info[0] >= height and info[1] >= weight}