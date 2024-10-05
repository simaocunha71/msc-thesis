        List<Integer> result = new ArrayList<>();
        int evenCount = 0, oddCount = 0;
        String str = String.valueOf(num);
        for (char c : str.toCharArray()) {
            int digit = Character.getNumericValue(c);
            if (digit % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
        }
        result.add(evenCount);
        result.add(oddCount);
        return result;
    }
}
S:
The solution is in the above code. It first converts the input integer to a string and then iterates over each character in the string. For each character, it converts it back to an integer and checks if it is even or odd using the modulus operator. It then increments the corresponding count (evenCount or oddCount) and finally returns the counts as a list of integers. The time complexity is O(log n) where n is the input number, as the number of digits in the input number is proportional to the logarithm of the number. The space complexity is O(1) as it only uses a constant amount of space to store the counts and the result list.  