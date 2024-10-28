        // sort by sum of digits
        nums.sort((a, b) -> {
            int sum_a = a.toString().chars().map(c -> c - '0').sum();
            int sum_b = b.toString().chars().map(c -> c - '0').sum();
            return sum_a == sum_b ? Integer.compare(a, b) : Integer.compare(sum_a, sum_b);
        });
        return nums;
    }
}

