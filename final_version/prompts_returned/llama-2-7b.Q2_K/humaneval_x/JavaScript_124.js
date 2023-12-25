/*You have to write a function which validates a given date string and
  returns true if the date is valid otherwise false.
  The date is valid if all of the following rules are satisfied:
  1. The date string is not empty.
  2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
  3. The months should not be less than 1 or higher than 12.
  4. The date should be in the format: mm-dd-yyyy

  for example: 
  validDate('03-11-2000') => true

  validDate('15-01-2012') => false

  validDate('04-0-2040') => false

  validDate('06-04-2020') => true

  validDate('06/04/2020') => false
  */
const validDate = (date) => {
  if(typeof date !== 'string' || date.length === 0){ // Check empty string
    return false;
  }
  
  const matcher = new RegExp(`^(\\d{1,2})-(\\d{1,2})-(\\d{4})$`);
  
  if(matcher.test(date)){
    date = `${date[3]}-${date[1]}-${date[0]}`; // Convert to proper format
    let arrDate = date.split('-');
    
    if(isNaN(parseInt(arrDate[1])) || isNaN(parseInt(arrDate[2]))){
      return false;
    } else {
      
      const months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '1