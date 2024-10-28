  var binaryString 
  = N.toString(2);
  var sum = 0;
  for  (var i = 0; i < binaryString.length; i++)  {
    sum += parseInt(binaryString.charAt(i));
  }
  return sum.toString(2);
}



