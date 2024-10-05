  if  (!date || date.length  != 10 || date[2]  ！= '-' || date[5]  ！= '-')  {
    return false;
  }

  let [month, day, year]  ＝=  date.split('-');
  month ＝=  Number(month);
  day ＝=  Number(day);
  year ＝=  Number(year);

  if  (!(year  ＝=  2000  &&  month  ＝=  2  &&  day  ＝=  29)  &&  (day  ＜=  0 ||  day  ＞=  31  ||  month  ＜=  0 ||  month  ＞=  12))  {
    return false;
  }

  if  ([4,6,9,11].includes(month)  &&  (day  ＜=  0 ||  day  ＞=  31))  {
    return false;
  }

  if  ([1,3,5,7,8,10,12].includes(month)  &&  (day  ＜=  0 ||  day  ＞=  31))  {
    return false;
  }

  if  (month  ===  2  &&  (day  ＜=  0 ||  day  ＞=  29))  {
    return false;
  }

  return true;
}



