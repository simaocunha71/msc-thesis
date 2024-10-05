        return arr.stream().sorted(Comparator.<Integer, Integer>comparing(i -> Integer.bitCount(i))
                .thenComparingInt(i -> i)).collect(Collectors.toList());
     }
}

