  let smallestEvenValueIndex = -1;
  let smallestEvenValue = Infinity;

  for  (let i  in arr)  {
    const element = arr[i];
    if  (element % 2 === 0  &&  element < smallestEvenValue)  {
      smallestEvenValue = element;
      smallestEvenValueIndex = i;
    }
  }

  return smallestEvenValueIndex === -1 ? [] : [smallestEvenValue, smallestEvenValueIndex];
}



