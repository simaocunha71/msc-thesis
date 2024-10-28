        StringBuilder decoded = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'A') {
                if (i + 1 < s.length() && s.charAt(i + 1) == 'A') {
                    i++;
                    continue A;
                } else {
                    decoded.append('A');
                    continue;
                }
            } else {
                decoded.append(s.charAt(i));
            }
        }
        return decoded.toString();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println("String encoded: " + s.encodeCyclic("ABC"));
        System.out.println("String decoded: " + s.decodeCyclic(s.encodeCyclic("ABC")));
        System.out.println("String decoded: " + s.decodeCyclic(s.encodeCyclic("AAB")));
        System.out.println("String decoded: " + s.decodeCyclic(s.encodeCyclic("AAA")));
        System.out.println("String decoded: " + s.decodeCyclic(s.encodeCyclic("BBA")));
        System.out.println("String decoded: " + s.decodeCyclic(s.encodeCyclic("AAABB")));
        System.out.println("String decoded: " + s.decodeCyclic(s.encodeCyclic("AABAA")));
        System.out.println("String decoded: " + s.decodeCyclic(s.encodeCyclic("ABABA")));
    }
}
