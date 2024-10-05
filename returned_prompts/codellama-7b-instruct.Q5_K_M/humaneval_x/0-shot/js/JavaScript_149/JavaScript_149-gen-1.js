function list_sort(lst) {
  let sortedList = [];
  let odd = [];
  let even = [];
  for (let i = 0; i < lst.length; i++) {
    if (lst[i].length % 2 === 0) {
      even.push(lst[i]);
    } else {
      odd.push(lst[i]);
    }
  }
  let sortedEven = even.sort();
  let sortedOdd = odd.sort();
  let sorted = sortedEven.concat(sortedOdd);
  return sorted;
}


