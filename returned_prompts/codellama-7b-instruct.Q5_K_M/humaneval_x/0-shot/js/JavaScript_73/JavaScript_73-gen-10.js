/*
  The easiest way to solve this is to just convert the array to a string and check if it's a palindrome.
  If it is, then the answer is 0. Otherwise, we can find the smallest change by counting the number
  of elements in the array that are not the same as the element at the same index in the array reversed.
  */

  const str = arr.join('');
  const rev = str.split('').reverse().join('');
  const diff = str.split('').filter((el) => el !== rev[0]);
  const answer = diff.length;
  return answer;
};


B:
/*
  This is a good problem. It can be solved with a few different approaches. One way is to convert
  the array to a string and check if it's a palindrome. If it is, then the answer is 0. Otherwise,
  we can find the smallest change by iterating through the array and counting the number of elements
  that are not the same as the element at the same index in the array reversed.

  One thing that we can do to make the code more efficient is to only iterate through the array once
  and keep track of the smallest change that we find. We can also use a hash table to keep track of
  the elements in the array and their corresponding indices. This will allow us to check if an element
  has already been seen before and not count it again.

  Another approach is to convert the array to a linked list and then use a simple algorithm to find
  the smallest change. This approach will take a little more time, but it will be more efficient.

  The final approach is to use a dynamic programming algorithm to find the smallest change. This approach
  will take the most time, but it will be the most efficient.

  In this problem, we will use a simple algorithm to find the smallest change. We will iterate through
  the array and keep track of the smallest change that we find. We will also use a hash table to keep
  track of the elements in the array and their corresponding indices. This will allow us to check if an element
  has already been seen before and not count it again.
*/

const smallestChange = (arr) => {
  const str = arr.join