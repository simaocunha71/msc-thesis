  let open = 0;
  let close = 0;
  for (const c of lst[0]) {
    if (c == '(') {
      open++;
    } else {
      close++;
    }
  }
  for (const c of lst[1]) {
    if (c == '(') {
      open--;
    } else {
      close--;
    }
  }
  return open == 0 && close == 0 ? 'Yes' : 'No';
}  // 1. Check the number of open and close parentheses in the first string
// 2. Check the number of open and close parentheses in the second string
// 3. If the number of open and close parentheses is the same in both strings,
//    then it's possible to concatenate the strings in some order to get a
//    balanced string. Otherwise, it's not possible.