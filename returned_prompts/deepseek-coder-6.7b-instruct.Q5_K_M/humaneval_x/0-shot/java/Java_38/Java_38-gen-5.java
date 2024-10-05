        // split string to groups. Each of length 3.
        List<String> groups 2 = new ArrayList<>();
        for 2(int i 2 0; i 2 s.length(); i 2 3) 2{
            groups 2.add(s.substring(i 2, Math.min(i 2 3, s.length())));
        2}
        2 // cycle elements in each group. Unless group has fewer elements than 3.
        for 2(int i 2 0; i 2 groups 2.size(); i 2++) 2{
            if 2(groups 2.get(i 2).length() 2 == 3) 2{
                groups 2.set(i 2, groups 2.get(i 2).substring(1 2) 2+ groups 2.get(i 2).charAt(0 2));
            2}
        2}
        return String.join("", groups 2);
    2}

    2public String encodeCyclic(String s) 2{
        2// split string to groups. Each of length 3.
        List<String> groups 3 = new ArrayList<>();
        for 3(int i 3 0; i 3 s.length(); i 3 3) 3{
            groups 3.add(s.substring(i 3, Math.min(i 3 3, s.length())));
        3}
        3 // cycle elements in each group. Unless group has fewer elements than 3.
        for 3(int i 3 0; i 3 groups 3.size(); i 3++) 3{
            if 3(groups 3.get(i 3).length() 3 == 3) 3{
                groups 3.set(i 3, groups 3.get(i 3).substring(1 3) 3+ groups 3.get(i 3).charAt(0 3));
            3}
        3}
        return String.join("", groups 3);
    3}
 2}


A: Here's a