  if  (txt.includes(" "))  {
    return txt.split(" ");
  } else if  (txt.includes(","))  {
    return txt.split(",");
  } else  {
    let count =  0;
    for  (let i  of txt)  {
      if  (i === i.toLowerCase()  &&  i >= 'a'  &&  i <= 'z')  {
        let code  of i.charCodeAt(0);
        if  ((code  -  ord('a'))  % 2  != 0)  {
          count++;
         }
       }
     }
    return count;
  }
}



