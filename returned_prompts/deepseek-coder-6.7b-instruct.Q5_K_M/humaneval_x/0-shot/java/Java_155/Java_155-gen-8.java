        List<Integer> counts = new ArrayList<>(Arrays.asList(0, 0));
        num = Math.abs(num);
        
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                counts.set(0, counts.get(0) + 1);
            } else {
                counts.set(1, counts.get(1) + 1);
            }
            num = num / 10;
        }
        
        return counts;
    }
}

In the above code, we start by setting the count of even and odd digits to 0. We then take the absolute value of the input number, ensuring we handle negative numbers correctly. We enter a loop that continues until there are no more digits left to process.

In each iteration of the loop, we extract the rightmost digit of the number, and check if it's even or odd. If it's even, we increment the count of even digits by 1. If it's odd, we increment the count of odd digits by 1.

Finally, we remove the processed digit from the number and continue until there are no more digits left.

The result is returned as a List of two integers. The first integer represents the count of even digits, and the second integer represents the count of odd digits.
*/

// ----------
// Solution 2: Using String Conversion and Iteration
// ----------

