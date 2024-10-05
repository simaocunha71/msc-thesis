        String[] sentences = S.split("[.?!]");
        int count = 0;
        for (String sentence : sentences) {
            sentence = sentence.trim();
            if (sentence.startsWith("I")) count++;
        }
        return count;
    }
}

