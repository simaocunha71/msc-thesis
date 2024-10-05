        int count = 0;
        for (String sentence : S.split("[.?!]")) {
            if (sentence.startsWith("I")) count += 1;
        }
        return count;
    }
}

