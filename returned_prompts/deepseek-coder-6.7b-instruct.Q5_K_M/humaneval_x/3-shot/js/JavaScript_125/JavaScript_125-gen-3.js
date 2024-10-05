  if  (txt.includes(' '))  {
    return txt.split(' ');
  }  else if  (txt.includes(','))  {
    return txt.split(',');
  }  else  {
    let count =  0;
    for  (let c of txt)  {
      if  (c.toLowerCase()  !=  c.toUpperCase())  {
        let code =  c.charCodeAt(0)  -  'a'.charCodeAt(0);
        if  ((code  % 2)  !=  0)  {
          count  +=  1;
        }
      }
    }
    return count;
  }
}



