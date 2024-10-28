        return arr.stream()
                .sorted(Comparator.comparingInt((Integer x) -> Integer.bitCount(x))
                        .thenComparingInt(Integer::intValue))
                .collect(Collectors.toList());
     }
}

