  if  (!date)  {
    return false;
  }

  const parts = date.split('-');
  if  (parts.length  != 3)  {
    return false;
  }

  const month = parseInt(parts[0], 10);
  const day = parseInt(parts[1], 10);
  const year = parseInt(parts[2], 10);

  if  (!month  || month  >  12)  {
    return false;
  }
  if  (!day  || day  < 1)  {
    return false;
  }
  if  (!year)  {
    return false;
  }

  switch  (month)  {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
      if  (day  >  31)  {
        return false;
      }
      break;
    case 4:
    case 6:
    case 9:
    case 11:
      if  (day  >  30)  {
        return false;
      }
      break;
    case 2:
      if  ((year  %  400  === 0)  ||  (year  %  100  !==  0  &&  year  %  4  === 0))  {
        if  (day  >  29)  {
          return false;
        }
      } else  {
        if  (day  >  28)  {
          return false;
        }
      }
      break;
    default:
      return false;
  }

  return true;
}



