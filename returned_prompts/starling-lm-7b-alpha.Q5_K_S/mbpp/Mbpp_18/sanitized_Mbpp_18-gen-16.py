def remove_dirty_chars(main_str:str,dirty_str:str) -> str:
  for char in dirty_str:
    main_str = main_str.replace(char,'')
  return main_str