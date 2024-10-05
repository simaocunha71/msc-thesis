        int count = 0;
        String[] sentences = S.split("[.!?]");
        for (String sentence : sentences) {
            if (sentence.trim().toLowerCase().startsWith("i")) {
                count += 1;
            }
        }
        return count;
    }
}

