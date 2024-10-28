  if  (n ≤ 0)  {
    return 0;
  } else if  (n ≤ 2)  {
    return 1;
  }

  let  fibfib_0  = 0;
  let  fibfib_1  = 1;
  let  fibfib_2  = 1;
  let  fibfib_n  = 0;

  for  (let i  =  3; i ≤ n; i++)  {
    fibfib_n  =  fibfib_0  +  fibfib_1  +  fibfib_2;
    fibfib_0  =  fibfib_1;
    fibfib_1  =  fibfib_2;
    fibfib_2  =  fibfib_n;
  }

  return  fibfib_n;
}



