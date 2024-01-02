/*Write a function that takes an array of numbers as input and returns 
  the number of elements in the array that are greater than 10 and both 
  first and last digits of a number are odd (1, 3, 5, 7, 9).
  For example:
  specialFilter([15, -73, 14, -15]) => 1 
  specialFilter([33, -2, -3, 45, 21, 109]) => 2
  */
const specialFilter = (nums) => {
  let length = nums.length;
  let result = 0;
   for(let i=0;i<length;i++){
       if(parseInt(nums[i]).toString().split('').pop() %2 === 1 && parseInt(nums[i]).toString().split('').shift() >10){
           result++
        }
   }
    return result;
}
console.log(specialFilter([-1,15,14,-3]));