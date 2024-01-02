/*Given a list of positive integers x. return a sorted list of all 
  elements that hasn't any even digit.

  Note: Returned list should be sorted in increasing order.
  
  For example:
  >>> uniqueDigits([15, 33, 1422, 1])
  [1, 15, 33]
  >>> uniqueDigits([152, 323, 1422, 10])
  []
  */
const uniqueDigits = (x) => {
    let xSorted = x.sort((a, b) => a - b);   //sorting the list in ascending order with the help of sort() funtion from Array.prototype and using a and b as parameters to sort it
    let evenDigits = [];     //storing the even digits into evenDigits array
  for (let i = 0; i < xSorted.length; i++) {   //iterating over every number in the list, and if the current element contains even digit then pushing that value to evenDigit array
    let currDigit = parseInt(xSorted[i].toString().split("").pop()) % 2;    //extracting the last digit of each number and checking whether it is an even or odd digit. If its 0 ,then its an even digit else its odd.
    if (currDigit == 1) {       //if its odd then pushing that value to even digits array
      evenDigits.push(xSorted[i]);  
    }  
  }                                //then returning the evenDigit array without changing any value in xSorted Array..
  return evenDigits;   
}