/*
  In this Kata, you have to sort an array of non-negative integers according to
  number of ones in their binary representation in ascending order.
  For similar number of ones, sort based on decimal value.

  It must be implemented like this:
  >>> sortArray([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
  >>> sortArray([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
  >>> sortArray([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
  */
const sortArray = (arr) => {
  let i = 0;
  while(i < arr.length){
    j = i + 1;
    while (j < arr.length && arr[j].toString().indexOf('1') != -1){
      if (arr[i] > arr[j]){
        let temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
      }else if(arr[i].toLocaleString() < arr[j].toLocaleString()){
        i++;
      }else{
        j++;
      }
    }
  }
  return arr.sort((a, b)=>{
    let aNumber = parseInt(a);
    let bNumber = parseInt(b);
    if (aNumber == bNumber) {
      return aNumber - bNumber;
    } else {
      return aNumber - bNumber;
    }
  });
}
