        StringBuilder sb = new StringBuilder();
        for  (char ch  :  s.toCharArray())  {
            sb.append((char)  ('a'  - ((ch  - 5  -  'a')  % 26)));
        }
        return sb.toString();
     }
}

