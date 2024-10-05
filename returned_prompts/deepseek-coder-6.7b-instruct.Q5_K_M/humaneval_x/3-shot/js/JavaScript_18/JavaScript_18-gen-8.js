  let count = 0;
  let position = 0;

  while  (true)  {
    position = string.indexOf(substring, position);
    if  (position  != -1)  {
      count += 1;
      position += 1;
    }  else  {
      break;
    }
  }

  return count;
}



