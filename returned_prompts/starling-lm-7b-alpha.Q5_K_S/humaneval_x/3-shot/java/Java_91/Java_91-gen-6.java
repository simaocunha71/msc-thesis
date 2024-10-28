        List<String> sentences = Arrays.asList(S.split("[.,!?]"));
        int result = 0;
        for (String sentence : sentences) {
            if (sentence.startsWith("I")) {
                result += 1;
            }
        }
        return result;
    }
}

