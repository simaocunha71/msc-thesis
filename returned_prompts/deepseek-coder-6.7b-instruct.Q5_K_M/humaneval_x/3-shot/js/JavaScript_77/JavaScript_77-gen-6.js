  let lower = 0;
  let upper = a;
  while  (lower <= upper)  {
    let mid = Math.floor((lower + upper) / 2);
    let cube = mid * mid * mid;
    if  (cube == a)  {
      return true;
     } else if  (cube < a)  {
      lower = mid + 1;
     } else  {
      upper = mid - 1;
     }
  }
  return false;
}



