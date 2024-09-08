  let even = [];
  let odd = [];
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] % 2 == 0) {
      even.push(lst[i]);
    } else {
      odd.push(lst[i]);
    }
  }
  let result = 0;
  for (let i = 0; i < even.length; i++) {
    if (i % 2 == 1) {
      result += even[i];
    }
  }
  return result;
}



