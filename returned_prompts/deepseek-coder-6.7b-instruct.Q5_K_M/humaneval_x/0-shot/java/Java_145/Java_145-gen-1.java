        List<Integer> result = new ArrayList<>(nums);
        Collections.sort(result, new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                int sum1 = sumOfDigits(a);
                int sum2 = sumOfDigits(b);
                if (sum1 == sum2) {
                    return nums.indexOf(a) - nums.indexOf(b);
                } else {
                    return sum1 - sum2;
                }
            }
        });
        return result;
    }

    public int sumOfDigits(int num) {
        int sum = 0;
        while (num != 0) {
            sum += Math.abs(num % 10);
            num /= 10;
        }
        return sum;
    }
}

This solution sorts the list based on the sum of the digits of the numbers. If the sums are equal, it orders them based on their original positions in the list. The helper function sumOfDigits calculates the sum of the digits of a number.

The time complexity of this solution is O(n log n), where n is the number of elements in the list. This is because we use the sort function from Collections, which has a time complexity of O(n log n). The space complexity is O(n), as we create a new list that is a copy of the original list.

This solution handles negative numbers correctly by using Math.abs to get the absolute value of each digit.
*/

//