        Comparator<Integer> comparator = new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                int ones_o1 = Integer.bitCount(o1);
                int ones_o2 = Integer.bitCount(o2);

                if (ones_o1 != ones_o2) return Integer.compare(ones_o1, ones_o2);
                return Integer.compare(o1, o2);
            }
        };
        Collections.sort(arr, comparator);
        return arr;
    }
}

