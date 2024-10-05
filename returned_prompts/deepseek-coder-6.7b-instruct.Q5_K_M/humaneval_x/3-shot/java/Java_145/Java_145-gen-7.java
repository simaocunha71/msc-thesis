        return nums.stream()
            .sorted(Comparator.comparing((Integer num) -> {
                int sum = 0;
                while (num != 0) {
                    sum += num % 10;
                    num /= 10;
                }
                return sum;
            }))
            .collect(Collectors.toList());
    }
}

