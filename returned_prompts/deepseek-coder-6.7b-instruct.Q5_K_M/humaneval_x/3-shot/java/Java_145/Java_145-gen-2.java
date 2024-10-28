        return nums.stream()
                .sorted(Comparator.comparingInt(i -> Math.abs(i.toString().chars().sum() - '0' * i.toString().length())))
                .collect(Collectors.toList());
     }
}

