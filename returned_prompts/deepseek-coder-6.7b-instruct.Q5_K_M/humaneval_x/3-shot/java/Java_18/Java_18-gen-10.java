        int count = 0;
        int idx 0;

        while  ((idx = string.indexOf(substring, idx)) != -1)  {
            count++;
            idx++;
        }

        return count;
     }
}

