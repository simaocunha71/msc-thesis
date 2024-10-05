        int count = 0;
        int index = 0;

        while  ((index  = string.indexOf(substring, index))                                                                             != -1)  {
            index  += substring.length();
            count++;
        }
        return count;
     }
}

