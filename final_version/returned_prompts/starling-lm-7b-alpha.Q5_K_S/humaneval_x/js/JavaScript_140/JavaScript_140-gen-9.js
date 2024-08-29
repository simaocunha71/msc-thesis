  let result = text.replace(/\s/g, '_');
  let last_space_index = result.lastIndexOf('_');
  while (last_space_index != -1) {
    if (result.charAt(last_space_index - 1) == '_' && result.charAt(last_space_index + 1) == '_') {
      result = result.substring(0, last_space_index) + '-' + result.substring(last_space_index + 1);
      last_space_index = result.lastIndexOf('_');
    } else {
      last_space_index = result.lastIndexOf('_');
    }
  }
  return result;
}



