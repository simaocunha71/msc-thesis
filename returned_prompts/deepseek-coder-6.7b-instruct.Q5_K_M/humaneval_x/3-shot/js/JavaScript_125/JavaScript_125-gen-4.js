  if  (txt.indexOf(' ')  != -1)  {
    return txt.split(' ');
  } else if  (txt.indexOf(',')  != -1)  {
    return txt.split(',');
  } else  {
    let count =  0;
    for  (let i  of txt)  {
      if  ((i.charCodeAt(0)  % 2)  != 0)  {
        count += 1;
       }
     }
    return count;
   }
 }



