        int count = 0;
        String[] sentences = S.split("[.!?\\s]+");
        for (String sentence : sentences) {
            if (sentence.trim().startsWith("I")) {
                count++;
            }
        }
        return count;
    }
}

