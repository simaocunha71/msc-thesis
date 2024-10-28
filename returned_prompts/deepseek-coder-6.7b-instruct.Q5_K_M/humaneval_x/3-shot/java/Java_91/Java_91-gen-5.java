        int count = 0;
        String[] sentences = S.split("[.|?|!]");
        for (String sentence : sentences) {
            if (sentence.trim().length() > 0 && sentence.trim().split(" ")[0].equals("I")) {
                count++;
            }
        }
        return count;
     }
}

