  let smallestEvenValueIndex = -1;
  let smallestEvenValue = Infinity;

  for  (let i = 0; i < arr.length; i++)  {
    if  (arr[i] < smallestEvenValue  && arr[i] % 2 == 0)  {
      smallestEvenValue = arr[i];
      smallestEvenValueIndex = i;
    }
  }

  return smallestEvenValueIndex != -1 ? [smallestEvenValue, smallestEvenValueIndex] : [];
}



