import java.util.*;

class Solution {
    public List<Integer> uniqueDigits(List<Integer> x) {
        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            if (hasNoEvenDigits(num)) {
                result.add(num);
            }
        }
        result.sort((a, b) -> Integer.compare(a, b));
        return result;
    }

    private boolean hasNoEvenDigits(int num) {
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                return false;
            }
            num /= 10;
        }
        return true;
    }
} 

Explanation:
The problem requires us to create a function that takes a list of positive integers and returns a sorted list of all elements that do not have any even digits.

The solution uses a helper function `hasNoEvenDigits` to check if a given number has any even digits. This function iterates through the digits of the number, and if it finds an even digit, it returns false. If it goes through all the digits without finding an even digit, it returns true.

The main function `uniqueDigits` iterates through the input list, checks each number using the helper function, and adds the numbers that do not have any even digits to the result list. Finally, it sorts the result list in ascending order and returns it.

The time complexity of this solution is O(n*m), where n is the number of elements in the input list and m is the maximum number of digits in the input integers. The space complexity is O(n), as we need to store the result list. 





