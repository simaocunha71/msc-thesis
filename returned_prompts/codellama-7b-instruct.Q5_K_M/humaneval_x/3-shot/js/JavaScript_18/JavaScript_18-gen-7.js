  var count = 0;
  var current_index = 0;

  while (current_index != -1) {
    current_index = string.indexOf(substring, current_index);
    if (current_index == -1) {
      break;
    }
    count += 1;
    current_index += substring.length;
  }

  return count;
}



