        List<Integer> result = new ArrayList<>(arr);
        result.sort((a, b) -> {
            if (Integer.bitCount(a) == Integer.bitCount(b)) {
                return a - b;
            } else {
                return Integer.bitCount(a) - Integer.bitCount(b);
            }
        });
        return result;
    }
}

