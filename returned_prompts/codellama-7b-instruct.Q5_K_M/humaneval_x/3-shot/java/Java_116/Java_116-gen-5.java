        List<Integer> result = new ArrayList<>();

        // sort by number of ones
        arr.sort((i, j) -> {
            int i_ones = Integer.bitCount(i);
            int j_ones = Integer.bitCount(j);
            return Integer.compare(i_ones, j_ones);
        });

        // sort by decimal value
        arr.sort((i, j) -> {
            int i_dec = i.intValue();
            int j_dec = j.intValue();
            return Integer.compare(i_dec, j_dec);
        });

        result.addAll(arr);
        return result;
    }
}

