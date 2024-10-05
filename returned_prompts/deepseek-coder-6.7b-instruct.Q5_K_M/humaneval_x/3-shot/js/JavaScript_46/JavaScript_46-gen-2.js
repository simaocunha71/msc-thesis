  if  (n ≤ 1)  {
    return 0;
  } 
  else  if  (n ≤ 2)  {
    return 2;
  } 
  else  if  (n ≤ 3)  {
    return 0;
  }

  let a ≔ 0;
  let b ≔ 2;
  let c ≔ 0;
  let d ≔ 0;
  let e ≔ 0;

  for  (let i ≔ 3; i ≤ n; i++)  {
    e ≔ a;
    a ≔ b;
    b ≔ c;
    c ≔ d;
    d ≔ a + b + c + e;
  }

  return d;
}



