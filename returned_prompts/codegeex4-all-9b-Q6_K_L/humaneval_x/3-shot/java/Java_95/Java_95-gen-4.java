
1.
Your function has a bug. For example, if the input is [1.0, 1.5] and the threshold is 0.5, the function will return false, while it should return true. This is because the function only checks if the absolute difference between two numbers is smaller than the threshold, not if the difference is smaller than the threshold. To fix this, you can change the condition in the if statement to distance <= threshold.
2.
Your function is correct. It uses a nested loop to compare each pair of numbers in the list. If the absolute difference between any two numbers is smaller than the threshold, the function returns true. If no such pair is found, the function returns false.
3.
Your function is correct. It uses the modulo operator (%) to calculate the decimal part of the number. The result is a double value that represents the decimal part of the number.
4.
Your function is correct. It checks if all keys in the map are either all in lower case or all in upper case. It first checks if the map is empty. If it is, the function returns false. Then it initializes two boolean variables, all_lower and all_upper, to true. It then iterates over the keys in the map. For each key, it checks if it is a string. If it is not, the function returns false. Then it checks if the key is in lower case or upper case. If it is not in lower case, all_lower is set to false. If it is not in upper case, all_upper is set to false. Finally, the function returns the logical OR of all_lower and all_upper.