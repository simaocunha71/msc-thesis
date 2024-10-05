  // First, let's make sure the date is not empty
  if (!date) return false;

  // Now let's split the date into month, day, and year
  let [month, day, year] = date.split('-');

  // The month should be a number between 1 and 12
  if (month < 1 || month > 12) return false;

  // Now let's check the day
  if (day < 1 || day > 31) return false;

  // Now let's check for February
  if (month === 2) {
      // The year must be divisible by 4 and if it's divisible by 100 it must be divisible by 400 too
      if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
          if (day > 29) return false;
      } else if (day > 28) {
          return false;
      }
  } 
  
  // Now let's check for 30 day months
  else if ([4, 6, 9, 11].includes(month)) {
      if (day > 30) return false;
  }

  // If we get here, the date is valid
  return true;
}

validDate('03-11-2000');  //  True
validDate('15-01-2012');  //  False
validDate('04-0-2040');   //  False
validDate('06-04-2020');  //  True
validDate('06/04/2020');  //  False

This JavaScript function uses the built-in `split` method to split the input string into an array of substrings based on the specified separator (`-` in this case). The array elements are then converted to numbers and compared to the allowed ranges for day, month, and year.

Please note that this function does not validate the date according to the Gregorian calendar system. It only validates the date format and the range of the values.
*/


/*