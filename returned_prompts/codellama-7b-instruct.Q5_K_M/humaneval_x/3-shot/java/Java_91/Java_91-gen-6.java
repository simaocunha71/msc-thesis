        int boredoms = 0;
        StringBuilder sentence = new StringBuilder();

        for (char c : S.toCharArray()) {
            if (c == '.' || c == '?' || c == '!') {
                if (sentence.toString().startsWith("I")) {
                    boredoms += 1;
                }
                sentence.setLength(0);
            }
            sentence.append(c);
        }
        return boredoms;
    }
}

