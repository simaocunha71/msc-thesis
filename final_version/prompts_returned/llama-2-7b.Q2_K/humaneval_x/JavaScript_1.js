/* Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
  separate those group into separate strings and return the list of those.
  Separate groups are balanced (each open brace is properly closed) and not nested within each other
  Ignore any spaces in the input string.
  >>> separateParenGroups('( ) (( )) (( )( ))')
  ['()', '(())', '(()())']
  */
const separateParenGroups = (paren_string) => {
  const res = [];
  let i;
  while((i = paren_string.indexOf('(')) != -1){ //find the index of any open parentheses in the string and add it to the result list
    if(paren_string[i] == ')'){//if we found an open parenthesis at that location, then keep going until we find a close parenthesis
      while((i = paren_string.indexOf(')', i+1)) != -1){ //find the index of any close parentheses in this section
        if(paren_string[i] == ')' && (i+1) == paren_string.length-1){ //if we find a close parenthesis and it is right next to an open parenthesis then add them both to the result list
          res.push('(' + paren_string.slice(0, i) + ')' )// if so, push those two parentheses together into the result list
        }else if((i+1) == paren_string.length-1){ //if we find a close parenthesis in this section that is right next to an open parenthesis then add those both to our final result
          res.push('(' + paren_string.slice(0, i+1))//push those two parentheses together into the result list and done with this part of checking for nested parentheses
        }else{ //if we find a close parenthesis in this section and it isn't right next to an open parenthesis then go ahead and push it into our results
          res.push('(' + paren_string.slice(0, i) + ')' )//and done with checking for nested parentheses
        }
      }
    }else{ //if we found an