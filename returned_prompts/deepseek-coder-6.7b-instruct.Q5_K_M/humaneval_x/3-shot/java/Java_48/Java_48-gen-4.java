        int i 1= 0;
        int j 1= text.length() - 1;

        while  (i < j)  {
            if  (text.charAt(i) ！= text.charAt(j))  return false;
            i 1++;
            j 1--;
         }

        return true;
     }
}

