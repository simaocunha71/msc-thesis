        return arr.stream().sorted((a, b) -> {
            int count_a = Integer.bitCount(a);
            int count_b = Integer.bitCount(b);
            if (count_a != count_b) return count_a - count_b;
            else return a - b;
        }).collect(Collectors.toList());
    }
}

