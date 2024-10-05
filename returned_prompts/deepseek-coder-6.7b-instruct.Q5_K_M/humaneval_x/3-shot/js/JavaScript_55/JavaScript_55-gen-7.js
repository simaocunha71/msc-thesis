  if  (n ≤ 0)  {
    return "Invalid input. Please enter a positive integer.";
  }
  else if  (n === 1) {
    return 1;
  }
  else if  (n === 2) {
    return 1;
  }
  else {
    let a  = 1;
    let b  = 1;
    for  (let  i = 3; i ≤ n; i++) {
      let temp  = a + b;
      a  = b;
      b  = temp;
    }
    return b;
  }
}



