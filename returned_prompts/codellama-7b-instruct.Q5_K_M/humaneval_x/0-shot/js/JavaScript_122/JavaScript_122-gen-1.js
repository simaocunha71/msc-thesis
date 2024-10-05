  const add = (num, digits) => {
    let result = num;

    for (let i = 0; i < digits; i++) {
      result += num;
    }
    return result;
  };

  let sum = 0;

  for (let i = 0; i < k; i++) {
    if (arr[i].toString().length <= 2) {
      sum += arr[i];
    }
  }

  return sum;
};

const testArr = [111, 21, 3, 4000, 5, 6, 7, 8, 9];

console.log(addElements(testArr, 4));

// 6
