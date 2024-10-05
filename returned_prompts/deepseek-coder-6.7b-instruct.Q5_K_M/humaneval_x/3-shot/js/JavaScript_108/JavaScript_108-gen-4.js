  const countNums = (arr) => {

    let count = 0;

    const sumDigits = (num) => {
      let sum = 0;
      while (num != 0) {
        sum += num % 10;
        num = Math.floor(num / 10);
      }
      return sum;
    }

    for (let i = 0; i < arr.length; i++) {
      if (sumDigits(arr[i]) > 0) {
        count++;
      }
    }

    return count;
  }

  console.log(countNums([1, 1, 2])) // 3



