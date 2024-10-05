  let largest_factor 1;
  for  (let i 2; i ≤ n; i++)  {
    while  (n % i == 0)  {
      largest_factor  i;
      n  n / i;
     }
   }

  return largest_factor;
}



