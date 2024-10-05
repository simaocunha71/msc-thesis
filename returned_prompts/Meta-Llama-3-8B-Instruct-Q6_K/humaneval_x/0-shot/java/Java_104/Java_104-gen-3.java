    public List<Integer> uniqueDigits(List<Integer> x) {
        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            if (!hasEvenDigit(num)) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }

    private boolean hasEvenDigit(int num) {
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                return true;
            }
            num /= 10;
        }
        return false;
    }
}  // This solution works by iterating over the list of numbers and for each number, it checks if it has any even digits. If it doesn't, it adds it to the result list. After all numbers have been processed, it sorts the result list and returns it. The hasEvenDigit method is a helper method that checks if a number has any even digits. It does this by repeatedly taking the last digit of the number (using the modulus operator), checking if it's even, and then removing the last digit (using integer division). If it finds an even digit, it returns true. If it doesn't find any even digits after processing all digits, it returns false.  // This solution has a time complexity of O(n*m) where n is the number of elements in the list and m is the maximum number of digits in a number. This is because for each number, it checks each digit to see if it's even. The space complexity is O(n) because it needs to store the result list.  // The hasEvenDigit method has a time complexity of O(m) where m is the maximum number of digits in a number. This is because it needs to process each digit to see if it's even. The space complexity is O(1) because it only uses a constant amount of space.  // The sorting operation has a time complexity of O(n log n) where n is the number of elements in the result list. The space complexity is O(n) because it needs to store the result list.  // Overall, the time complexity is O(n*m) + O(n log n) = O(n*m + n log n) and the space complexity is O(n) + O(1) = O(n).  // The solution is correct because it correctly identifies the numbers that don't have any even digits and returns them in a sorted list. It also handles the case where the input list is