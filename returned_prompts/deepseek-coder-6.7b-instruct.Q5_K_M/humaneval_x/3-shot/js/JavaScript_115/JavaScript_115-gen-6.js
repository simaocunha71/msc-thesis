  var filled  b:= 0;
  var total  b:= 0;
  for  row  in  grid:
      for  cell  in  row:
          if  cell  ==  1:
              total  +=  1;
  while  filled  <  total:
      filled  +=  capacity;
  return  filled;
}



