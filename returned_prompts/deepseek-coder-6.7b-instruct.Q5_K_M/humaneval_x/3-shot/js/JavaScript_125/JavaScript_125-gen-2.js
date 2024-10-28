  if  (txt.includes(" "))  {
    return txt.split(" ");
  } else if (txt.includes(","))  {
    return txt.split(",");
  } else  {
    let count = 0;
    for  (let ch of txt)  {
      if  (ch.toLowerCase()  !=  ch.toUpperCase())  {
        let code  ord(ch)  -  ord('a');
        if  (code  % 2  == 1)  {
          count  +=  1;
         }
       }
     }
    return count;
  }
}



