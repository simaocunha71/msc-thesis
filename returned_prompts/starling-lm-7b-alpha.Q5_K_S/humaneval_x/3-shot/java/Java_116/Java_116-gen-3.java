        Collections.sort(arr, (a, b) -> {
            int a_bit_count = Integer.bitCount(a);
            int b_bit_count = Integer.bitCount(b);
            if (a_bit_count != b_bit_count) return Integer.compare(a_bit_count, b_bit_count);
            return Integer.compare(a, b);
        });
        return arr;
    }
}


```