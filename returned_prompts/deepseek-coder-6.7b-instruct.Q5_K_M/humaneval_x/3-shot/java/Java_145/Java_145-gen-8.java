        return nums.stream()
                .sorted(Comparator.comparingInt(i -> i < 0 ? -i : i))
                .collect(Collectors.toList());
     }
}

