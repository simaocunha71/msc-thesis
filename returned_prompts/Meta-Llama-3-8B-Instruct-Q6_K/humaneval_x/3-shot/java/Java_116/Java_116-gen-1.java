        List<Integer> result = new ArrayList<>();
        Collections.sort(arr, new Comparator<Integer>() {
            public int compare(Integer a, Integer b) {
                int countA = Integer.toBinaryString(a).replace("1", "").length();
                int countB = Integer.toBinaryString(b).replace("1", "").length();
                return Integer.compare(countA, countB);
            }
        });
        return arr;
    }
}

