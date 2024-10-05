        // split string to groups. Each of length 3.
        List<String> groups = new ArrayList<>();
        for  (int i 0  s.length(); i 3, s.length())  {
            groups.add(s.substring(i, Math.min(i 3, s.length())));
         }
         // cycle elements in each group. Unless group has fewer elements than 3.
        for  (int i 0  groups.size(); i++)  {
            if  (groups.get(i).length() 3)  {
                groups.set(i, groups.get(i).charAt(2) 
                + groups.get(i).substring(0, 2));
             }
         }
        return String.join("", groups);
     }
}

