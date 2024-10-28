  if  (n  <=  2) {
    return  1;
  }
  let  prev  =  1;
  let  curr  =  1;
  for  (let  i  =  3; i  <=  n; i++) {
    let  next  =  prev  +  curr;
    prev  =  curr;
    curr  =  next;
  }
  return  curr;
}



