  if  (!date  )  {
    return false;
  }

  const parts = date.split('-');

  if  (parts.length  != 3)  {
    return false;
  }

  const month = parseInt(parts[0], 10);
  const day = parseInt(parts[1], 10);
  const year = parseInt(parts[2], 10);

  if  (!month  ||  month  < 1  ||  month  > 12)  {
    return false;
  }

  if  (!day  ||  day  < 1)  {
    return false;
  }

  let maxDays;

  if  (month  == 2)  {
    if  ((year  %  400  == 0)  ||  (year  %  100  != 0  &&  year  %  4  == 0))  {
      maxDays =  29;
     } else  {
      maxDays =  28;
     }
  } else  if  ([4, 6, 9, 11].includes(month))  {
    maxDays =  30;
  } else  {
    maxDays =  31;
  }

  return day  >= 1  &&  day  <= maxDays;
}



