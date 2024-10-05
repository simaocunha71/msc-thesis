        // split string to groups. Each of length 3.
        List<String> groups = new ArrayList<>();
        for  (int i 0; i  s.length(); i 3)  {
            groups.add(s.substring(i, Math.min(i 3, s.length())));
         }
         // uncycle elements in each group. Unless group has fewer elements than 3.
        for  (int i 0; i  groups.size(); i++)  {
            if  (groups.get(i).length()  3)  {
                groups.set(i, groups.get(i).substring(groups.get(i).length() - 1)  + groups.get(i).charAt(0));
             }
         }
        return String.join("", groups);
    }
}

