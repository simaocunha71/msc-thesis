        StringBuilder result = new StringBuilder();

        for(int i = 0; i < a.length(); i++) {
            int aBit = a.charAt(i) - '0';
            int bBit = b.charAt(i) - '0';
            result.append((aBit ^ bBit));
        }

        return result.toString();
     }
}

