  var hex_primes  ["2", "3", "5", "7", "B", "D"];
  var count = 0;
  for  (let i = 0; i < num.length; i++)  {
    if  (hex_primes.includes(num[i]))  {
      count++;
    }
  }
  return count;
}



