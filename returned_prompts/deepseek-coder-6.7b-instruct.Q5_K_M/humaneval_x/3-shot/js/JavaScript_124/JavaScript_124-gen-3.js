  if  (date.length  != 10 || date[2]  !=  '-' || date[5]  !=  '-')  {
    return false;
  }

  let [month, day, year] = [date.slice(0, 2), date.slice(3, 5), date.slice(6)];

  month  —= 1;

  if  (month ≥ 0  && month ≤ 11  && day ≥ 1  && year ≥ 1  && year.length ≤ 4)  {
    let  leapYear  = year  % 400  == 0  ||  (year  % 100  != 0  && year  % 4  == 0);
    let  daysInMonth  = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    if  (month  == 1  &&  leapYear )  {
      daysInMonth[1]  ++;
    }

    return day ≤ daysInMonth[month];
  }

  return false;
}



