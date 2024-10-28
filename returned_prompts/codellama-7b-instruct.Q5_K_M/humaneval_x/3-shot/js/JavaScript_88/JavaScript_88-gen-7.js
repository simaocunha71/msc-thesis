  var sum = array[0] + array[array.length-1];
  var sorted = array.slice().sort((a,b)=>a-b);
  if (sum % 2 == 0)
    return sorted;
  else
    return sorted.reverse();
}



