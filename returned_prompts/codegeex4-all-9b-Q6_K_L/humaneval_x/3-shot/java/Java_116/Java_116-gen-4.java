        arr.sort((a, b) -> {
            int a_ones = Integer.bitCount(a);
            int b_ones = Integer.bitCount(b);

            if (a_ones == b_ones) {
                return Integer.compare(a, b);
            } else {
                return Integer.compare(a_ones, b_ones);
            }
        });
        return arr;
    }
}

