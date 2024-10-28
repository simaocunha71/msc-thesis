  var stack =  [];
  for  (const bracket of brackets)  {
    if  (bracket == "<")  {
      stack.push(bracket);
    } else if  (bracket == ">")  {
      if  (stack.length  && stack[stack.length  - 1] == "<")  {
        stack.pop();
       } else  {
        return false;
       }
     }
   }

  return  stack.length  ?  false  :  true;
}



