        int count = 0;
        String[] sentences = S.split("[.?!]");
        for (String sentence : sentences) {
            if (sentence.trim().startsWith("I")) count += 1;
        }
        return count;
    }
}

