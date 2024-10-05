        int boredomCount = 0;
        String[] sentences = S.split("[.!?]+");

        for (String sentence : sentences) {
            if (sentence.trim().startsWith("I")) {
                boredomCount++;
            }
        }
        return boredomCount;
    }
}

