
def extract_singly(list_of_lists):
  extracted_nums = set()
  for sub_list in list_of_lists:
    for num in sub_list:
      extracted_nums.add(num)
  return extracted_nums


