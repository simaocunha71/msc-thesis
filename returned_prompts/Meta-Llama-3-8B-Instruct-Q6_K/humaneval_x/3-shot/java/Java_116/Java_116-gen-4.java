        Collections.sort(arr, new Comparator<Integer>() {
            public int compare(Integer a, Integer b) {
                String aBinary = Integer.toBinaryString(a);
                String bBinary = Integer.toBinaryString(b);

                int aOnes = countOnes(aBinary);
                int bOnes = countOnes(bBinary);

                if (aOnes == bOnes) {
                    return a.compareTo(b);
                } else {
                    return Integer.compare(aOnes, bOnes);
                }
            }

            private int countOnes(String binary) {
                int count = 0;
                for (char c : binary.toCharArray()) {
                    if (c == '1') {
                        count++;
                    }
                }
                return count;
            }
        });
        return arr;
    }
}

