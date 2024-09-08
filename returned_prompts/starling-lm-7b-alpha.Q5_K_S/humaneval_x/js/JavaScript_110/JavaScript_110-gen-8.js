  let count = 0;
  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 === 0) {
      count += 1;
    }
  }
  if (count === lst1.length) {
    return 'YES';
  }
  for (let j = 0; j < lst2.length; j++) {
    if (lst2[j] % 2 === 0) {
      count += 1;
    }
  }
  if (count >= lst1.length) {
    return 'YES';
  } else {
    return 'NO';
  }
}



