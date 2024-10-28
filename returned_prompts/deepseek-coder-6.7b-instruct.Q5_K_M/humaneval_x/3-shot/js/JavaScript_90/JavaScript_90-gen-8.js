  let min = null;
  let second_min = null;

  for  (let i = 0; i < lst.length; i++)  {
    if  (min === null || lst[i] < min)  {
      second_min = min;
      min = lst[i];
    }  else if  (lst[i] > min && (second_min === null || lst[i] < second_min))  {
      second_min = lst[i];
    }
  }

  return second_min;
}



