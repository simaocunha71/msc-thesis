/*"
  This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
  multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
  change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
  
  Examples:
  For lst = [1,2,3] the output should be 6
  For lst = []  the output should be 0
  For lst = [-1,-5,2,-1,-5]  the output should be -126
  */
const sumSquares = (lst) => {
    let i = 0;
    while(i<lst.length && lst[i]!==null){
      if(Math.floor((i-3)/3)) //checks if the index is divisible by 3, and if so, calculates its square (in this case) then sets that to a value in the array
        lst[i]=lst[i]*(Math.pow(i%3,2));
      else
        i++; //sets i to the next integer after the one the square was calculated for
    }//loop ends when all values are checked and the condition is met
  return lst;
}
