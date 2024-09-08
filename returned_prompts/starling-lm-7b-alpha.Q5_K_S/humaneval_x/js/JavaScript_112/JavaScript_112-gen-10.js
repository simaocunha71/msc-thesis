  let result = s;
  for (let i = 0; i < c.length; i++) {
    while (result.indexOf(c[i]) >= 0) {
      result = result.replace(c[i], '');
    }
  }

  let left = 0;
  let right = result.length - 1;
  while (left < right) {
    if (result[left] != result[right]) {
      return (result, false);
    }
    left++;
    right--;
  }
  return (result, true);
}



