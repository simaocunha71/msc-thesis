/*

  Move One Ball:

  You are given an array of integers. You are allowed to move one ball from one
  position to another position. Each position can only be occupied by one ball.
  
  You want to move the ball from the last position to the first position. You are
  allowed to move the ball from the position i to the position i+1 or i-1.
  
  If you move the ball from the position i to the position i+1, then the position
  i will be empty.
  
  If you move the ball from the position i to the position i-1, then the position
  i will be occupied by another ball.
  
  If you move the ball from the position i to the position i+1, then the position
  i-1 will be occupied by another ball.
  
  Given an array of integers, return true if it is possible to move the ball
  from the last position to the first position, otherwise return false.
  
  If the given array is empty, return true.
  
  For Example:
  
  moveOneBall([3, 4, 5, 1, 2])==>true
  Explanation:
  move the ball from position 4 to position 3,
  move the ball from position 5 to position 2,
  move the ball from position 1 to position 0
  
  moveOneBall([3, 5, 4, 1, 2])==>false
  Explanation:
  move the ball from position 5 to position 4,
  move the ball from position 4 to position 3,
  move the ball from position 1 to position 0
  
  moveOneBall([])==>true
  Explanation:
  Return true since the array is empty.

  */
const moveOneBall = (arr) => {

C:
/*

  Maximum Number:

  You are given an array of integers. Your task is to find the maximum number in 
  the array.
  
  For Example:
  
  maxNumber([1, 2, 3, 4, 5])==>5
  Explanation: The maximum number