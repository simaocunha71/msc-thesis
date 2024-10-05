        StringBuilder sb = new StringBuilder();
        for  (char ch  :  s.toCharArray())  {
            sb.append((char) ('a' + ((ch - 'a' - 5 + 26) % 26)));
         }
        return sb.toString();
     }
}

