/*Write a function that takes an array of numbers as input and returns 
  the number of elements in the array that are greater than 10 and both 
  first and last digits of a number are odd (1, 3, 5, 7, 9).
  For example:
  specialFilter([15, -73, 14, -15]) => 1 
  specialFilter([33, -2, -3, 45, 21, 109]) => 2
  */
const specialFilter = (nums) => {
  let arr = [];
  for(let i=0;i< nums.length;i++){
    if((-1*nums[i] - 2 >= 15 && (-1*nums[i] + 3 <= 14))){
      console.log("Special Filters",arr); //Return Array
      break;
    }else{
      arr = [...arr, nums[i]]; // Add the number to array if it is a special one and it doesn't already exist in the array
    }
  }
}

specialFilter([15, -73, 14, -15]);
