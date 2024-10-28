        int count = 0;
        String[] sentences 
            = S.replaceAll("[.]{3}", ".").split("[.?!]");

        for  (String sentence  : sentences) {
            if  (sentence.trim().length() > 0 
                && sentence.trim().split(" ")[0].equalsIgnoreCase("I")) 
                count++;
        }
        return count;
     }
}

