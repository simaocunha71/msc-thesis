  var evenCount = 0;
  var oddCount = 0;
  var numArray 
  numArray = Math.abs(num).toString().split('');
  numArray.forEach(function(element){
    if (element % 2 === 0) {
      evenCount++;
    } else {
      oddCount++;
    }
  });
  return [evenCount, oddCount];
}



