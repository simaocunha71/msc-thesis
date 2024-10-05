

  const allEven = (lst) => {
    for (let i = 0; i < lst.length; i++) {
      if (lst[i] % 2 !== 0) {
        return false;
      }
    }
    return true;
  };
  const isEven = (num) => num % 2 === 0;

  if (lst1.length === 0 || lst2.length === 0) return "NO";

  let isEvenLst1 = allEven(lst1);
  let isEvenLst2 = allEven(lst2);

  if (isEvenLst1 && isEvenLst2) {
    return "YES";
  }

  const arr = [];
  for (let i = 0; i < lst2.length; i++) {
    arr.push(lst2[i]);
  }

  const arr2 = [];
  for (let i = 0; i < lst1.length; i++) {
    arr2.push(lst1[i]);
  }

  let isEven = false;

  for (let i = 0; i < arr.length; i++) {
    if (isEvenLst1) {
      break;
    }
    for (let j = 0; j < arr2.length; j++) {
      if (isEvenLst2) {
        break;
      }
      if (isEvenLst1 || isEvenLst2) {
        break;
      }
      if (isEven(arr[i]) && isEven(arr2[j])) {
        isEven = true;
        lst1.splice(j, 1);
        lst2.splice(i, 1);
        break;
      }
    }
  }

  if (isEven) {
    return "YES";
  }

  return "NO";
};

// let list1 = [1, 2, 3, 4];
// let list2 = [1, 2, 3, 4];
// console.