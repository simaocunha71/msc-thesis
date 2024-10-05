  if  (strings.length == 0)  {
    return null;
  }
  var longest_string = strings[0];
  for  (const string of strings)  {
    if  (string.length > longest_string.length)  {
      longest_string = string;
    }
  }
  return longest_string;
}



