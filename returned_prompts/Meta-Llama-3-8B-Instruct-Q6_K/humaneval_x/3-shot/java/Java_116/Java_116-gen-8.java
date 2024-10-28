        Collections.sort(arr, new Comparator<Integer>() {
            public int compare(Integer a, Integer b) {
                int countA = Integer.bitCount(a);
                int countB = Integer.bitCount(b);
                if (countA == countB) {
                    return a.compareTo(b);
                } else {
                    return Integer.compare(countA, countB);
                }
            }
        });
        return arr;
    }
}

