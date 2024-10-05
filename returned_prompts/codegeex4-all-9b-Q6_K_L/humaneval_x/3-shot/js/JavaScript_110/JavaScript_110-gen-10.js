  var odd_nums = [];
  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 != 0) {
      odd_nums.push(lst1[i]);
    }
  }
  for (let i = 0; i < lst2.length; i++) {
    if (lst2[i] % 2 == 0) {
      for (let j = 0; j < odd_nums.length; j++) {
        if (lst2[i] == odd_nums[j]) {
          odd_nums.splice(j, 1);
        }
      }
    }
  }
  if (odd_nums.length == 0) {
    return 'YES';
  } else {
    return 'NO';
  }
}