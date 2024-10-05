        Collections.sort(arr, new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                String binaryA = Integer.toBinaryString(a);
                String binaryB = Integer.toBinaryString(b);

                int onesA = binaryA.length() - binaryA.replace("1", "").length();
                int onesB = binaryB.length() - binaryB.replace("1", "").length();

                if (onesA == onesB) {
                    return a - b;
                } else {
                    return onesA - onesB;
                }
            }
        });
        return arr;
    }
}

