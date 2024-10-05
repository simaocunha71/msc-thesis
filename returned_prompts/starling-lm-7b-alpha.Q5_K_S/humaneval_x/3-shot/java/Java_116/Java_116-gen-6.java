        Comparator<Integer> binary_ones = new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                int a_ones = Integer.bitCount(a);
                int b_ones = Integer.bitCount(b);
                if (a_ones != b_ones) {
                    return Integer.compare(a_ones, b_ones);
                } else {
                    return Integer.compare(a, b);
                }
            }
        };
        Collections.sort(arr, binary_ones);
        return arr;
    }
}



```