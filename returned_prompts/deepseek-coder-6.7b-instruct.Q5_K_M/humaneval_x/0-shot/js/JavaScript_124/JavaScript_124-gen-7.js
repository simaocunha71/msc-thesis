  const dateRegex = /^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{4})$/;
  if (!date.match(dateRegex)) return false;

  const [month, day, year] = date.split('-').map(Number);
  
  if (month === 2) {
    if (day > 29) return false;
  } else if ([4,6,9,11].includes(month)) {
    if (day > 30) return false;
  } else if ([1,3,5,7,8,10,12].includes(month)) {
    if (day > 31) return false;
  } else if ([2].includes(month)) {
    if (day > 28) return false;
  }

  return true;
}

Explanation:
In the function validDate, first, we check if the date string matches the regex pattern `mm-dd-yyyy`. If it doesn't, we return false. Then, we split the date string into month, day, and year, and convert them to numbers.

Then, we check if the day is greater than the maximum number of days allowed for the specific month. If it is, we return false.

Finally, if none of the above conditions are met, we return true, indicating that the date is valid.
*/









































































































































































