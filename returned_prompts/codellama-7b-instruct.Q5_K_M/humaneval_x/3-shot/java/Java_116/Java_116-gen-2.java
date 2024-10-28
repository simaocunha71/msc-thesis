        return arr.stream().sorted((a, b) -> {
            int a_ones = Integer.bitCount(a);
            int b_ones = Integer.bitCount(b);
            if (a_ones != b_ones) return a_ones - b_ones;
            return a - b;
        }).collect(Collectors.toList());
    }
}

