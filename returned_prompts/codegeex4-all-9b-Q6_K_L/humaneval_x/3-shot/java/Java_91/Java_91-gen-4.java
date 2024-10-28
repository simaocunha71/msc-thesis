        String[] sentences = S.split("\\.");
        int count = 0;
        for (String sentence : sentences) {
            sentence = sentence.trim();
            if (sentence.length() > 0 && sentence.startsWith("I")) {
                count += 1;
            }
        }
        return count;
    }
}

