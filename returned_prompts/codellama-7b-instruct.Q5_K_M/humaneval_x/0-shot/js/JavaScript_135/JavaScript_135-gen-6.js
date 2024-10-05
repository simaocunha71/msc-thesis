
function canArrange(arr){

  for(let i = 0; i < arr.length; i++){
    if(arr[i] >= arr[i - 1]){
      return i - 1;
    }
  }
  return -1;
}

console.log(canArrange([1, 2, 4, 3, 5]));

