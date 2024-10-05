  for  (let i = 0; i < numbers.length; i++) {
    for  (let j = 0; j < numbers.length; j++) {
      if  (i ！= j) {
        let 距离 = Math.abs(numbers[i] - numbers[j]);
        if  (距离 < 阈值) {
          return true;
         }
       }
     }
   }
  return false;
}



