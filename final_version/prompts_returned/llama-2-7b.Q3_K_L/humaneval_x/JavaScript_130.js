/*Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
  the last couple centuries. However, what people don't know is Tribonacci sequence.
  Tribonacci sequence is defined by the recurrence:
  tri(1) = 3
  tri(n) = 1 + n / 2, if n is even.
  tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
  For example:
  tri(2) = 1 + (2 / 2) = 2
  tri(4) = 3
  tri(3) = tri(2) + tri(1) + tri(4)
         = 2 + 3 + 3 = 8 
  You are given a non-negative integer number n, you have to a return a list of the 
  first n + 1 numbers of the Tribonacci sequence.
  Examples:
  tri(3) = [1, 3, 2, 8]
  */
const tri = (n) => {
    let retList = [];
    if(n == -1 ) return [];
    else{
      for(let i = 0;i < n+1;i++){
        if((i%2) === 0){
          retList.push(tri(i-1));}else {
            if (i % 3 !== 0 && i % 4 !== 0 && i % 5 !== 0) {
              retList = retList.concat([tri(i - 1)]);
            } else {
              let currentIndex = retList.length;
              for(let j = 1;j < (i-1)/2+1;j++){
                if((j%3 != 0 || j % 4 == 0) && (j%5 != 0)){ //check for every odd number and then check for even number
                  let tempList = [];
                  retList[currentIndex] +=tri(i-j)+tri(i-1+j);//calculating two different numbers
                  
                }else{ 
                  if((j%3 !=