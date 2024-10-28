        String[] sentences = S.split("[\\.\\?\\!]");
        int count = 0;

        for (String sentence : sentences) {
            if (sentence.trim().toLowerCase().startsWith("i")) {
                count += 1;
            }
        }
        return count;
    }
}

