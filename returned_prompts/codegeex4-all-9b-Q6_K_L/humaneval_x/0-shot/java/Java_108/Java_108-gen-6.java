public int countNums(List<Integer> arr) {
        int count = 0;
        for (int num : arr) {
            int sum = 0;
            boolean isNegative = false;
            if (num < 0) {
                isNegative = true;
                num = -num;
            }
            while (num > 0) {
                sum += num % 10;
                num /= 10;
            }
            if (isNegative) {
                sum = -sum;
            }
            if (sum > 0) {
                count++;
            }
        }
        return count;
    }