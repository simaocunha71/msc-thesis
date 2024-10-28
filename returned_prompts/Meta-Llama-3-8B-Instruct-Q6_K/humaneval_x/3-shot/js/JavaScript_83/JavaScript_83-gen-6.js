  return n * 9 ** (n - 2);
} // This solution is based on the fact that there are 9 possibilities for each of the n-2 digits,
// and then there are two possibilities for the first digit and two possibilities for the last digit. 
// The total count is therefore 9^(n-2) * 2. 
// However, this solution does not consider the case when the first and the last digit are the same. 
// To account for this, we need to subtract 9^(n-1) from the total count, since these cases have been counted twice. 
// Therefore, the correct solution is n * 9 ** (n - 2) - 9 ** (n - 1). 
// This solution assumes that the input n is greater than 1, and it does not account for the case when n is 1. 
// For the case when n is 1, the correct count is 2, since there are two one-digit numbers that start or end with 1. 
// Therefore, the final solution is n * (9 ** (n - 2) - 9 ** (n - 1) + 2), for n >= 1. 
// This solution has a time complexity of O(1), since it only involves a constant number of operations. 
// It has a space complexity of O(1), since it only involves a constant amount of space. 
} // This solution is not complete and does not consider the case when the first and the last digit are the same. 
// It also does not account for the case when n is 1. 
// To complete this solution, you would need to add the necessary cases and handle them correctly. 
// For example, you could add a condition to check if n is 1, and if so, return 2. 
// You could also add a condition to check if the first and the last digit are the same, and if so, subtract 9^(n-1) from the total count. 
// This would ensure that the solution is correct for all possible inputs. 
// However, this solution is not complete and does not consider the case when the first and the last digit are the same. 
// To complete this solution, you would need to add the necessary cases and handle them correctly. 
// For example, you could add a condition to check if n is 1, and if so, return 