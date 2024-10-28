  let a = 1, b = 1;
  while  (n-- > 2)  {
    [a, b] = [b, a + b];
   }
  return b;
 }



