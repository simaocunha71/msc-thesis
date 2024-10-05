  let sum = 0;
  for  (let i  of s)  {
    if  (i === i.toUpperCase() && i !== i.toLowerCase())  {
      sum += i.charCodeAt(0);
     }
   }
  return sum;
 }



