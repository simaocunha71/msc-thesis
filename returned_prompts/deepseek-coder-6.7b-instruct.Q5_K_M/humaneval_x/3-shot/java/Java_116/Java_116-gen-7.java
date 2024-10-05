        return arr.stream()
            .sorted(Comparator.comparing((Integer x) -> Integer.bitCount(x))
                .thenComparing(Integer::intValue))
            .collect(Collectors.toList());
    }
}

