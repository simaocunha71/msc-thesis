        // sort based on number of ones in binary representation
        Comparator<Integer> comparator = (Integer a, Integer b) -> {

            int a_ones = Integer.bitCount(a);
            int b_ones = Integer.bitCount(b);
            if (a_ones != b_ones) return a_ones - b_ones;
            else return a - b;
        };

        Collections.sort(arr, comparator);
        return arr;
    }
}

