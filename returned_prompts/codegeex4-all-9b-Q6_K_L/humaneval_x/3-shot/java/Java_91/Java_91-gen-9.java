        String[] sentences = S.split("[.!?]");
        int count = 0;
        for (String sentence : sentences) {
            if (sentence.trim().startsWith("I")) {
                count += 1;
            }
        }
        return count;
    }
}

