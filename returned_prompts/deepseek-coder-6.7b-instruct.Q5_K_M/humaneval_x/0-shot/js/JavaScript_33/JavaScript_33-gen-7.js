  let newArr = [];
  let tempArr = [];

  for (let i = 0; i < l.length; i++) {
    if (i % 3 === 0) {
      tempArr.push(l[i]);
    } else {
      newArr.push(l[i]);
    }
  }

  tempArr.sort((a, b) => a - b);

  for (let i = 0; i < l.length; i++) {
    if (i % 3 === 0) {
      newArr.splice(i, 0, tempArr.shift());
    }
  }

  return newArr;
}


console.log(sortThird([1, 2, 3])) // [1, 2, 3]
console.log(sortThird([5, 6, 3, 4, 8, 9, 2])) // [2, 6, 3, 4, 8, 9, 5]

*/



/*
