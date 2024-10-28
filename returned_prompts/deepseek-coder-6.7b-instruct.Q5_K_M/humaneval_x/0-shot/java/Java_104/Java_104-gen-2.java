        List<Integer> result = new ArrayList<>();
        for (Integer num : x) {
            if (!hasEvenDigit(num)) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }

    private boolean hasEvenDigit(Integer num) {
        while (num > 0) {
            if ((num % 10) % 2 == 0) {
                return true;
            }
            num /= 10;
        }
        return false;
    }
}

This code first creates a new list to store the results. It then iterates over each number in the input list, and checks if any of its digits are even using the hasEvenDigit method. If the method returns false, the number is added to the results list. Finally, the results list is sorted and returned.

The hasEvenDigit method works by iterating over each digit of the number, checking if it's even, and returning true if any are. If it gets through all the digits without finding an even one, it returns false.
