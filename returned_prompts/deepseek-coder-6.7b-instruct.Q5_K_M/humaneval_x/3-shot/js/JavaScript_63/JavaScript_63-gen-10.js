  if  (n  === 0)  {
    return 0;
  } else if  (n  === 1)  {
    return 0;
  } else if  (n  === 2)  {
    return 1;
  } else  {
    let  a  =  0;
    let  b  =  0;
    let  c  =  1;
    for  (let  i  =  2; i  <  n; i++)  {
      let  temp  =  a  +  b  +  c;
      a  =  b;
      b  =  c;
      c  =  temp;
    }
    return  c;
  }
}



