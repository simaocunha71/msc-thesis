  if  (n < 2)  {
    return false;
  }
  for  (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++) {
    if  (n % i === 0)  {
      return false;
     }
   }
  return true;
}



