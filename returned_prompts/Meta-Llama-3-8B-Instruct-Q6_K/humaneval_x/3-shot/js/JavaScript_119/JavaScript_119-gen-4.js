  let open = 0, close = 0;
  for (let i = 0; i < lst[0].length; i++) {
    if (lst[0][i] == '(') open++;
    if (lst[0][i] == ')') close++;
  }
  for (let i = 0; i < lst[1].length; i++) {
    if (lst[1][i] == '(') open--;
    if (lst[1][i] == ')') close--;
  }
  if (open == 0 && close == 0) return 'Yes';
  return 'No';
}