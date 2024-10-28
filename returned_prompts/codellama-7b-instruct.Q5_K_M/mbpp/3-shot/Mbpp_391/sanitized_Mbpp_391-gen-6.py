def convert_list_dictionary(sid,names,marks):
  dict_list = []
  for i in range(len(sid)):
    dict_list.append({sid[i]:{names[i]:marks[i]}})
  return dict_list