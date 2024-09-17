def get_ludic(max_num: int) -> list:
  ludic_list = [1]
  ludic_num = 2
  while ludic_num <= max_num:
    is_lucid = True
    for ludic in ludic_list:
      if ludic_num % ludic == 0:
        is_lucid = False
        break
    if is_lucid:
      ludic_list.append(ludic_num)
    ludic_num += 1
  return ludic_list