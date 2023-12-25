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
  const arrayOfBinaryRepresentation = arr.map((item)=>('0b' + item).split(''));
  let sortedNums;
  if (!arrayOfBinaryRepresentation[0].includes('1')){
    return ['-1'];
  }else{
    for (let j = 0;j<arrayOfBinaryRepresentation.length;j++){
      const binaryNum = arrayOfBinaryRepresentation[j];
      let sortDecimals = '';
      if(binaryNum && Array(1).includes('1')){ // if it contains at least one '1', we can order by decimal value
        for (let k = 0;k<binaryNum.length;k++){
          const binaryValue = binaryNum[k];
          sortDecimals += parseInt(binaryValue * 450, 2) + parseInt('0b' + k); // sort based on decimal value of ones and zeros
        }
      }else{
        for (let i=j+1;i<arrayOfBinaryRepresentation.length;i++) {
          const oneBefore = arrayOfBinaryRepresentation[i];
          let oneBeforeSort = 0;
          for(let k=binaryNum.length-1;k>=0;k--){
            if (oneBefore[(k+1)%4] === '1'){ // look at the value in 'one before' (binary representation of the number) that follows zeroes and ones, and