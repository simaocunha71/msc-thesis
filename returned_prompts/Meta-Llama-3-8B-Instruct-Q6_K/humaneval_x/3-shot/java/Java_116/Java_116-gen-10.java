        Collections.sort(arr, new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                int onesA = Integer.toBinaryString(a).replace("0", "").length();
                int onesB = Integer.toBinaryString(b).replace("0", "").length();
                if (onesA == onesB) {
                    return a.compareTo(b);
                } else {
                    return Integer.compare(onesA, onesB);
                }
            }
        });
        return arr;
    }
}

