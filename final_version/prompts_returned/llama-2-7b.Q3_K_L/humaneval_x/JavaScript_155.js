/*Given an integer. return a list that has the number of even and odd digits respectively.

   Example:
      evenOddCount(-12) ==> [1, 1]
      evenOddCount(123) ==> [1, 2]
  */
const evenOddCount = (num) => {
    let sumEven = 0;
    let sumOdd = 0;
    
    let n = num.toString();
    console.log(n);
    n = n.split('').reverse().join('');
    let arr = n.split('');
    let count = (arr[0] + "").length %2 == 1 ? 1 : 0;
    
    for(let i = 1; i < arr.length; i++){
      console.log("i: "+i);
        if((arr[i]+"").length %2 == 0){
          sumEven += count;
            count = (arr[i+1] + "").length %2 == 1 ? 1 : 0;
        }else{
          sumOdd += count;
            arr.shift();
            count = (arr[i]+"").length %2 == 0 ? 1 : 0;
        }    
    }
    return [sumEven, sumOdd];
}
