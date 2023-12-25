/*In this problem, you will implement a function that takes two lists of numbers,
  and determines whether it is possible to perform an exchange of elements
  between them to make lst1 a list of only even numbers.
  There is no limit on the number of exchanged elements between lst1 and lst2.
  If it is possible to exchange elements between the lst1 and lst2 to make
  all the elements of lst1 to be even, return "YES".
  Otherwise, return "NO".
  For example:
  exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
  exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
  It is assumed that the input lists will be non-empty.
  */
const exchange = (lst1, lst2) => {
  if(lst1[0] % 2 !== 0 || lst2[0] % 2 !== 0 ){
    return "NO"
}else{
  var indexOfOddElement = findIndex(lst1, i=>i%2);
  var indexOfEvenElement = findIndex(lst1, i=>! (i % 2));
  
  if(indexOfOddElement === -1 || indexOfEvenElement === -1 ){
    return "NO"
  }else{
    lst1[indexOfEvenElement] += lst1[indexOfOddElement];
    lst1.splice(indexOfOddElement, 0, lst2);
    lst2.splice(indexOfOddElement, 0);
    
    return "YES"
  }
}
function findIndex(arr, callback) {
    for(let index = 0; index < arr.length; index++) {
        if (callback(index, arr)) {
            return index;
        }
    }
}
