        return arr.stream()
            .sorted(Comparator.comparing(i -> Integer.bitCount(i))
                .thenComparing(Integer::intValue))
            .collect(Collectors.toList());
    }
}

