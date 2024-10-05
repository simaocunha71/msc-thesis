  if  (xs.length  % 2  == 1)  {
    throw  new  Error('Only polynomials with even number of coefficients can have real roots');
  }

  let  a =  Math.max(...xs.slice(0, -1));

  if  (a  ==  0)  {
    throw  new  Error('Only polynomials with largest coefficient as it guarantees a solution can have real roots');
  }

  let  b  =  0.5  *  (Math.sqrt(a  *  a  - 4  *  xs[0]  *  xs[-1])  -  a);

  return  b  /  (2  *  xs[-1]);
}



