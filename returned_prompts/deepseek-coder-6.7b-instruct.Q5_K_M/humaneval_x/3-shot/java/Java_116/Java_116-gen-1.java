        return arr.stream()
            .sorted(Comparator.comparing(i -> Integer.bitCount(i))
                .thenComparingInt(i -> i))
            .collect(Collectors.toList());
     }
}

