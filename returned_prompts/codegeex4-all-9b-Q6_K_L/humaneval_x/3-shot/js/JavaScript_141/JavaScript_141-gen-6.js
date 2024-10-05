  let numberCount = 0;
  for (const c of file_name) {
    if (c >= '0' && c <= '9') {
      numberCount += 1;
    }
  }
  if (numberCount > 3) {
    return 'No';
  }
  let dotCount = 0;
  let dotIndex = -1;
  for (let i = 0; i < file_name.length; i++) {
    if (file_name[i] == '.') {
      dotCount += 1;
      dotIndex = i;
    }
  }
  if (dotCount != 1) {
    return 'No';
  }
  let beforeDot = file_name.substring(0, dotIndex);
  let afterDot = file_name.substring(dotIndex + 1);
  if (beforeDot.length == 0) {
    return 'No';
  }
  if (!(beforeDot[0] >= 'a' && beforeDot[0] <= 'z' || beforeDot[0] >= 'A' && beforeDot[0] <= 'Z')) {
    return 'No';
  }
  if (afterDot != 'txt' && afterDot != 'exe' && afterDot != 'dll') {
    return 'No';
  }
  return 'Yes';
}

What do you think? Are there any improvements I could make?