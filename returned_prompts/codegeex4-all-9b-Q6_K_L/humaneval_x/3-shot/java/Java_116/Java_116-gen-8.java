        Collections.sort(arr, (a, b) -> {
            int a_ones = Integer.bitCount(a);
            int b_ones = Integer.bitCount(b);
            return Integer.compare(a_ones, b_ones) == 0 ? Integer.compare(a, b) : Integer.compare(a_ones, b_ones);
        });
        return arr;
    }
}

