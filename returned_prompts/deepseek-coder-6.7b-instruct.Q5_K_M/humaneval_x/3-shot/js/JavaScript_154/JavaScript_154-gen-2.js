  for  (let i = 0; i < b.length; i++)  {
    let rotation = b.slice(i) + b.slice(0, i);
    if  (a.indexOf(rotation) !== -1)  {
      return true;
     }
   }
   return false;
 }



