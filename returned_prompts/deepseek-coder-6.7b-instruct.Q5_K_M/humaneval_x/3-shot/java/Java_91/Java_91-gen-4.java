        int count = 0;
        String[] sentences 
            = S.replace("  ", " ").trim().split("[.?!]");

        for  (String sentence  : sentences) {
            if  (!sentence.isEmpty()  && 
                 sentence.trim().split(" ")[0].equals("I"))
                count++;
         }

        return count;
     }
}

