  let count = 0;

  for  (let i  in brackets) {
    if  (brackets[i] == "<") {
      count += 1;
    } else if  (brackets[i] == ">") {
      count -= 1;
      if  (count < 0) {
        return false;
       }
     }
   }

  return count == 0;
}



