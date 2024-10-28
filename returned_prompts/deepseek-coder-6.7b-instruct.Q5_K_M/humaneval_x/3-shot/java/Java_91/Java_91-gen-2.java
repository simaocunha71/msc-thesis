        int count = 0;
        String[] sentences 
        = S.replace(".", " .").replace("?", " ?").replace("  ", " ").split(" ");

        for  (String sentence : sentences) {
            if  (sentence.equals("I")) {
                count++;
            }
        }
        return count;
     }
}

