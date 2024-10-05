  const arr1 = l1.sort();
  const arr2 = l2.sort();
  const newArr = [];

  for(let i = 0; i < arr1.length; i++) {
    if(arr1[i] === arr2[i] && !newArr.includes(arr1[i])) {
      newArr.push(arr1[i]);
    }
  }
  return newArr;
}

