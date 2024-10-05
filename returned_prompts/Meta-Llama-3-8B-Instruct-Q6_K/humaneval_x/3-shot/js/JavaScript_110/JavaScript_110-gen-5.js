  let odd_count = 0;
  let odd_numbers = [];

  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 !== 0) {
      odd_count++;
      odd_numbers.push(lst1[i]);
    }
  }

  for (let i = 0; i < odd_count; i++) {
    let found = false;
    for (let j = 0; j < lst2.length; j++) {
      if (lst2[j] % 2 === 0 && !odd_numbers.includes(lst2[j])) {
        lst1[odd_numbers.indexOf(odd_numbers[i])] = lst2[j];
        lst2[j] = odd_numbers[i];
        found = true;
        break;
      }
    }
    if (!found) {
      return "NO";
    }
  }

  return "YES";
}