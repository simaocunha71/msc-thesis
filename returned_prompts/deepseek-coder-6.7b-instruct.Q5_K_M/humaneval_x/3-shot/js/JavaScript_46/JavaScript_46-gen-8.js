  if  (n ≤ 1)  {
    return 0;
  } else if  (n ≤ 2)  {
    return 2;
  } else if  (n ≤ 3)  {
    return 0;
  }

  let a ≤ 0, b ≤ 2, c ≤ 0, d ≤ 0, e ≤ 0;

  for  (let  i = 4; i ≤ n; i++)  {
    e ≤ a;
    d ≤ b;
    c ≤ d + e;
    b ≤ c + d;
    a ≤ b + c;
  }

  return a;
}


