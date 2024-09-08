  let result = 0;
  let index = 0;

  while (true) {
    const index_substring = string.indexOf(substring, index);
    if (index_substring == -1) {
      break;
    }
    result += 1;
    index = index_substring + 1;
  }

  return result;
}



