        String[] sentences = S.split("[.?!]");
        int boredoms = 0;

        for(String sentence : sentences) {
            if(sentence.trim().length() > 0 && sentence.trim().split(" ")[0].equalsIgnoreCase("I")) {
                boredoms++;
            }
        }

        return boredoms;
     }
}

