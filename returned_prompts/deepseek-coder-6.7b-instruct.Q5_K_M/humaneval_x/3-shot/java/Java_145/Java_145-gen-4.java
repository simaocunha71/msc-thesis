        return nums.stream()
                .sorted(Comparator.comparingInt(i -> Integer.toString(Math.abs(i)).chars().sum()))
                .collect(Collectors.toList());
     }
}

