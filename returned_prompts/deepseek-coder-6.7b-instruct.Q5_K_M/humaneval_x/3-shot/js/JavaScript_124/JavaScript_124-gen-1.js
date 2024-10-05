  if  (date.length  != 10 || date[2]  !=  '-' || date[5]  !=  '-')  return false;
  
  let mm =  Number(date.slice(0, 2));
  let dd =  Number(date.slice(3, 5));
  let yyyy =  Number(date.slice(6, 10));

  if  (mm  <  1 || mm  >  12)  return false;
  if  (dd  <  1)  return false;

  let isLeapYear  (yyyy) => {
    return  (yyyy  %  4  === 0)  &&  ((yyyy  %  100  !=  0)  ||  (yyyy  %  400  ==  0));
  }

  let daysInMonth  [31,  isLeapYear(yyyy)  ?  29  :  28,  31,  30,  31,  30,  31,  31,  30,  31,  30,  31];

  return  dd  <=  daysInMonth[mm - 1];
}



