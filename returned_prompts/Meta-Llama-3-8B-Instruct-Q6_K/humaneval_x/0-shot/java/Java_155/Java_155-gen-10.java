        List<Integer> result = new ArrayList<>();
        int evenCount = 0;
        int oddCount = 0;
        
        String str = String.valueOf(num);
        for(int i = 0; i < str.length(); i++) {
            int digit = Integer.parseInt(String.valueOf(str.charAt(i)));
            if(digit % 2 == 0) {
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

The solution is quite straightforward. First, convert the input integer into a string. Then iterate over each character in the string, convert it back into an integer, and check if it is even or odd. If it is even, increment the even count, if it is odd, increment the odd count. Finally, return a list containing the even count and the odd count. 

The time complexity is O(n), where n is the number of digits in the input integer. The space complexity is O(1), as it only uses a constant amount of space to store the result and the counts. 





