  = parseInt(num.charAt(i), 16);
    if  (primes.includes(hexDigit))  {
      count++;
    }
  }
  return count;
}



