  let sum = 0;
  for(let i = 0; i < k; i++) {
      let num = arr[i];
      if(num >= 10 && num <= 99) {
          sum += num;
      }
  }
  return sum;
}



