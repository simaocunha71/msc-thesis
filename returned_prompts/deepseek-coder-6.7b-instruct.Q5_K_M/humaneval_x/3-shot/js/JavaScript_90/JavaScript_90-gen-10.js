  if  (lst.length  &&  lst.length  >  1)  {
    lst.sort((a, b) => a  - b);
    for  (let i  =  1; i  < lst.length; i++)  {
      if  (lst[i]  !=  lst[0])  {
        return lst[i];
       }
     }
   }
   return null;
 }



