  if  (strings.length  != 0)  {
    let longestString = strings[0];
    for  (let i=0; i<strings.length; i++)  {
      if  (strings[i].length  >  longestString.length)  {
        longestString = strings[i];
      }
    }
    return longestString;
  }
  else  {
    return null;
  }
}



