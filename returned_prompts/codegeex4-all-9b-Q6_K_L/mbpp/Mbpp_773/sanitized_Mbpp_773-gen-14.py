def occurance_substring(main_string,sub_string):
  if sub_string in main_string:
    return (sub_string,main_string.find(sub_string),main_string.rfind(sub_string))
  else:
    return None