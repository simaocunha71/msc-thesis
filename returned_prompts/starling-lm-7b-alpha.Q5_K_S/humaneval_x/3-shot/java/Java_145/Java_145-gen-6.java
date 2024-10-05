        Collections.sort(nums, new Comparator<Integer>() {
            @Override
            public int compare(Integer lhs, Integer rhs) {
                return sumOfDigits(lhs) - sumOfDigits(rhs);
            }
        });
        return nums;
    }

    private int sumOfDigits(int number) {
        int result = 0;
        while (number > 0) {
            result += number % 10;
            number /= 10;
        }
        return result;
    }
}

