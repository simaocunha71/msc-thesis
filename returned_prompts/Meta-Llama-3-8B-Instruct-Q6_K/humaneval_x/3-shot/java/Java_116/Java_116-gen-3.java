        Collections.sort(arr, new Comparator<Integer>() {
            public int compare(Integer a, Integer b) {
                int countA = Integer.toBinaryString(a).replace("1", "").length();
                int countB = Integer.toBinaryString(b).replace("1", "").length();
                if (countA == countB) {
                    return a.compareTo(b);
                } else {
                    return countA - countB;
                }
            }
        });
        return arr;
    }
}

