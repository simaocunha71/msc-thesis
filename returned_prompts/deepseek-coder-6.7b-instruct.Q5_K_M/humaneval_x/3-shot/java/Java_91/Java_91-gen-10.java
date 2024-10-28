        int count = 0;
        String[] sentences = S.split("[.?!]");

        for(String sentence: sentences){
            if(sentence.trim().length() > 0 && sentence.trim().charAt(0) == 'I'){
                count++;
            }
        }
        return count;
     }
}

