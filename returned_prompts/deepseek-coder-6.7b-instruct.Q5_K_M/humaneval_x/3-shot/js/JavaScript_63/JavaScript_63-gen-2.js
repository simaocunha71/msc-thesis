  if  (n ≤ 1)  {
    return 0;
  } 
  if  (n ≤ 2)  {
    return 1;
  } 

  let  fibfib_sequence  = [0, 0, 1];
  for  (let i = 3; i ≤ n; i++)  {
    fibfib_sequence[i] = fibfib_sequence[i-1] + fibfib_sequence[i-2] + fibfib_sequence[i-3];
  }

  return fibfib_sequence[n];
}



