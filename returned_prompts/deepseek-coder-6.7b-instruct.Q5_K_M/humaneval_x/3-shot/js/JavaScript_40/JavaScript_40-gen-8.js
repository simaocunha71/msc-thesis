  if  (l.length < 3)  {
    return false;
  }

  l.sort((a, b) => a - b);

  for  (let i = 0; i < l.length - 2; i++)  {
    let j = i + 1;
    let k = l.length - 1;

    while  (j < k)  {
      if  (l[i] + l[j] + l[k] === 0)  {
        return true;
     
      } else if  (l[i] + l[j] + l[k] < 0)  {
        j += 1;

      } else  {
        k -= 1;
       }
     }
   }

  return false;
}



