    let result = [numbers[0]];

    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] > numbers[i - 1]) {
            result.push(numbers[i]);
        } else {
            result.push(numbers[i - 1]);
        }
    }
    return result;
};






/* From a given list of integers, generate a list of rolling maximum element found until given moment
  in the sequence.
  >>> rollingMax([1, 2, 3, 2, 3, 4, 2])
  [1, 2, 3, 3, 3, 4, 4]
  */
const rollingMax = (numbers) => {

    let result = [numbers[0]];

    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] > numbers[i - 1]) {
            result.push(numbers[i]);
        } else {
            result.push(numbers[i - 1]);
        }
    }
    return result;
};




/* From a given list of integers, generate a list of rolling minimum element found until given moment
  in the sequence.
  >>> rollingMin([1, 2, 3, 2, 3, 4, 2])
  [1, 1, 1, 1, 1, 1, 1]
  */
const rollingMin = (numbers) => {

    let result = [numbers[0]];

    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] < numbers[i - 1]) {
            result.push(numbers[i]);
        } else {
            result.push(numbers[i - 1]);
        }
    }
    return result;
};


/* From a given list of integers, generate a list of rolling minimum element found until given moment
  in the sequence.
  >>> rollingMin([1, 2, 3