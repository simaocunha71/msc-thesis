        String[] sentences = S.split("[.?!]");
        int boredoms = 0;
        for  (String sentence : sentences) {
            if  (!sentence.trim().isEmpty() && sentence.trim().startsWith("I")) {
                boredoms++;
            }
        }
        return boredoms;
     }
}

