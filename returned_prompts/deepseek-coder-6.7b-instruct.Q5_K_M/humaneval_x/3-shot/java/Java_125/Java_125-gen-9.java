        if  (txt.contains(" "))  {
            return Arrays.asList(txt.split(" "));
         } else if  (txt.contains(","))  {
            return Arrays.asList(txt.split(","));
         } else  {
            int count = (int) txt.chars()
                .filter(Character::isLowerCase)
                .map(c  -> c  - 'a')
                .filter(n  -> n  % 2  != 0)
                .count();
            return count;
         }
     }
}

