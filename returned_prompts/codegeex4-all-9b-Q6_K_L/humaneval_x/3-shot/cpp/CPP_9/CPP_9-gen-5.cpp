
Q1: You are not initializing i and j in your loop. That is a common issue that can lead to undefined behavior. You should initialize your variables at the beginning of the block.

Q2: Your function is correct. It correctly separates the parentheses into separate groups. However, your code is not very efficient. You are looping through the entire string each time you add a parenthesis to the current group. You can improve your function by keeping track of the current level and only adding parentheses to the current group if the level is 0.

Q3: Your function is correct. It correctly truncates the decimal part of the number. However, your code is not very efficient. You are converting the number to an integer twice. You can improve your function by using the fmod function to get the decimal part of the number.

Q4: Your function is correct. It correctly generates a vector of rolling maximum elements. However, your code is not very efficient. You are looping through the entire vector each time you add a new element to the all_max vector. You can improve your function by keeping track of the current maximum and only updating it when you find a new maximum.

Overall, your code is correct and well-structured. However, there are some areas where you can improve your code for better performance and readability.