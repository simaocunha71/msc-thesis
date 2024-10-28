        return nums.stream()
            .sorted(Comparator.comparing((Integer num) -> sumOfDigits(num))
                .thenComparing(nums::indexOf))
            .collect(Collectors.toList());
    }

    private int sumOfDigits(int num) {
        int sum = 0;
        while (num != 0) {
            sum += Math.abs(num % 10);
            num /= 10;
        }
        return sum;
    }
}

