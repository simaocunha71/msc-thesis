        int count = 0;
        int index = 0;

        while  (true)  {
            index = string.indexOf(substring, index);
            if  (index  != -1)  {
                count += 1;
                index += substring.length();
             } else  break;
         }

        return count;
     }
}

