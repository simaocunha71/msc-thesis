def is_Sub_Array(main_list: list,sub_list: list) -> bool:
  return set(sub_list).issubset(set(main_list))

