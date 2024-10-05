        String[] sentences = S.split("[.?!]");
        int boredom = 0;
        for (String sentence : sentences) {
            if (sentence.trim().startsWith("I")) {
                boredom += 1;
            }
        }
        return boredom;
    }
}

