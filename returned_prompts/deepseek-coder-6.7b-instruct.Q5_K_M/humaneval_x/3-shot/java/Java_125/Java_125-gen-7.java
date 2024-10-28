        if  (txt.contains(" ")) {
            return Arrays.asList(txt.split(" "));
        } else if (txt.contains(",")) {
            return Arrays.asList(txt.split(","));
        } else {
            int count = 0;
            for  (char c  : txt.toCharArray()) {
                if  (Character.isLowerCase(c)  &&  ((int)c  -  (int)'a')  % 2  !=  0) count += 1;
             }
            return count;
         }
      }
}

