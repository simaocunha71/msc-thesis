        return nums.stream()
            .sorted(Comparator.comparingInt(i -> Integer.toString(Math.abs(i)).chars().sum()))
            .collect(Collectors.toList());
    }
}


A: Here are the corrections for your code:

