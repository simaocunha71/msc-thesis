  let sum = 0;
  for(let i=0; i<k; i++){
    if(arr[i] < 10 || arr[i] > 99){
      sum += arr[i];
    }
  }
  return sum;
}



