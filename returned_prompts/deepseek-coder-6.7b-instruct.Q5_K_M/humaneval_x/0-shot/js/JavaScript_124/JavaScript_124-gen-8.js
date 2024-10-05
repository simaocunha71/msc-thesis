  if(date.length === 0) return false;

  let [month, day, year] = date.split('-');

  if(month < 1 || month > 12 || day < 1 || year < 1) return false;

  if(month === '02'){
    if(day > 29) return false;
  }
  else{
    if( [1,3,5,7,8,10,12].includes(month) && day > 31 ) return false;
    if( [4,6,9,11].includes(month) && day > 30 ) return false;
    if( ![1,3,5,7,8,10,12].includes(month) && day > 31 ) return false;
  }

  return true;

};

console.log(validDate('03-11-2000')); // => true
console.log(validDate('15-01-2012')); // => false
console.log(validDate('04-0-2040'));  // => false
console.log(validDate('06-04-2020')); // => true
console.log(validDate('06/04/2020')); // => false

*/

const validDate = (date) => {
  if (date.length === 0) return false;

  let [month, day, year] = date.split("-");

  if (month < 1 || month > 12 || day < 1 || year < 1) return false;

  if (month === "02") {
    if (day > 29) return false;
  } else {
    if (
      ([1, 3, 5, 7, 8, 10, 12].includes(month) && day > 31) ||
      ([4, 6, 9, 11].includes(month) && day > 30) ||
      (![1, 3, 5, 7, 8, 10, 12].includes(month) && day > 31)
    )
      return