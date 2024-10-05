        Collections.sort(arr, new Comparator<Integer>() {
            public int compare(Integer a, Integer b) {
                int aOnes = Integer.toBinaryString(a).replace("0", "").length();
                int bOnes = Integer.toBinaryString(b).replace("0", "").length();
                if (aOnes == bOnes) {
                    return a - b;
                } else {
                    return aOnes - bOnes;
                }
            }
        });
        return arr;
    }
}

