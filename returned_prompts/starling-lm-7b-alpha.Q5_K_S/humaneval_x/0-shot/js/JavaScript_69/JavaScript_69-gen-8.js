To solve this problem, we can create a dictionary to store the frequency of each number in the list,
then traverse the dictionary in descending order and return the first number whose frequency is greater than or equal to its value.

Here is a step-by-step explanation of the solution:

1. We start by creating an empty dictionary called `freq`.
2. We iterate over the input list using the `forEach` method. For each element in the list, we check if it exists as a key in the `freq` dictionary. If it does, we increment its value by 1; if it doesn't, we initialize it to 1.
3. After calculating the frequency of each number in the list, we enter a for loop that starts from the length of the input list and decrements down to 1.
4. Inside the for loop, we check if the frequency of the current number (`i`) is greater than or equal to the value of `i`. If it is, we return `i` as the result. If none of the numbers satisfy this condition, we return -1 as the result.
5. Finally, we test the solution by calling the `search` function with different input lists and logging the results to the console.

By following these steps, we can find the greatest integer that has a frequency greater than or equal to its value in the input list.

*/






