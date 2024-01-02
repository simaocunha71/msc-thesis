/*Implement a function that takes an non-negative integer and returns an array of the first n
  integers that are prime numbers and less than n.
  for example:
  countUpTo(5) => [2,3]
  countUpTo(11) => [2,3,5,7]
  countUpTo(0) => []
  countUpTo(20) => [2,3,5,7,11,13,17,19]
  countUpTo(1) => []
  countUpTo(18) => [2,3,5,7,11,13,17]
  */
const countUpTo = (n) => {
  let i = 0;
  let arr = [];
  let tempArr = [];
  while(i < n){
    // console.log(arr);
   if(!isPrime(i)){
     tempArr = getPrimes(i,arr);
      for (let p of tempArr) {
        console.log('p',p);
        arr.push(p);
      }
   }
    i++;
  }
}
const isPrime= (num)=>{
if(num ===1 || num===0){
return false;
}else if((num%2)==0 ){
return false;
}else{
return true;
}
}
const getPrimes = (n,arr) => {
  let tempArr= [];
  for (let i of range(1, n)) {
    // console.log(`i=${i}`);
    if (!isPrime(i)) continue;
   if(!arrayIncludes(arr,i)){
     tempArr.push(i)
     arrayPush(arr, i);
   }else{
    arr = filterArr(arr, i );
  }
}
return tempArr;
};
const range=(n)=>{
for (let x of [...Array(n)]).map((item) => Number(item));
}
const arrayIncludes= (array1,array2) => {
  let isArrayEqual = true;
  for (let i of array2){
    if (!arrayIncluded(i