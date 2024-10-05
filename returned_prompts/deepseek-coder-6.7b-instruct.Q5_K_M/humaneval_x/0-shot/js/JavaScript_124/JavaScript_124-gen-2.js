  const dateRegex = /^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{4})$/;
  if(!dateRegex.test(date)) return false;

  let [month, day, year] = date.split('-');
  month = parseInt(month);
  day = parseInt(day);
  year = parseInt(year);

  if(month === 2) {
    if(day > 29) return false;
    if(day === 29 && !(year % 400 === 0 || (year % 100 !== 0 && year % 4 === 0))) return false;
  } else if([4,6,9,11].includes(month)) {
    if(day > 30) return false;
  } else if([1,3,5,7,8,10,12].includes(month)) {
    if(day > 31) return false;
  } else {
    if(day > 31) return false;
  }

  return true;
};

This solution works by first using a regex to check if the string is in the correct mm-dd-yyyy format. Then, it splits the date into the month, day, and year, converts them to integers, and checks if they meet the specified rules.
*/

const validDate = (date) => {
  const dateRegex = /^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{4})$/;
  if (!dateRegex.test(date)) return false;

  const [month, day, year] = date.split("-").map(Number);

  if ([1, 3, 5, 7, 8, 10, 12].includes(month) && day > 31) return false;
  if ([4, 6, 9, 11].includes(month) && day > 30) return false;
  if (month