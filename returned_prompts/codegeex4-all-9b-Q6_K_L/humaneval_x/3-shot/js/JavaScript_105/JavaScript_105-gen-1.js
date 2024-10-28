  let result = [];
  let numbers = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'];
  let sorted_arr = arr.sort((a,b) => a - b);
  let reversed_arr = sorted_arr.reverse();
  for (let i = 0; i < reversed_arr.length; i++) {
    let num = reversed_arr[i];
    if (num >= 1 && num <= 9) {
      result.push(numbers[num - 1]);
    }
  }
  return result;
}