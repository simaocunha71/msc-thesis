        int count = 0;
        int idx  ;
        while ((idx = string.indexOf(substring, count)) != -1) {
            count ++;
        }
        return count;
     }
}

