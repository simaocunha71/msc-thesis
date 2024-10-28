  if  (xs.length  % 2  == 0)  {
    throw  new Error("Polynomial must have odd number of coefficients");
  }
  let a = xs[0];
  if  (a  ==  0)  {
    throw  new Error("First coefficient can't be zero");
  }
  let b  xs[1]  /  a;
  let c  =  (b  *  b  -  xs[2]  /  a)  /  2;
  let d  c  *  c  -  xs[3]  /  a;
  return  Math.sqrt((c  *  c  -  d)  /  3)  *  -1  /  (b  /  3);
}



