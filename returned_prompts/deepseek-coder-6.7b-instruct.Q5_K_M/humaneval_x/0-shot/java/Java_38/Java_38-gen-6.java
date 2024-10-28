    List<String> groups 
            = new ArrayList<>();
    for (int i = 0; i < s.length(); i += 3) {
        groups.add(s.substring(i, Math.min(i + 3, s.length())));
    }
    for (int i = 0; i < groups.size(); i++) {
        if (groups.get(i).length() == 3) {
            groups.set(i, groups.get(i).charAt(2) + groups.get(i).substring(0, 2));
        }
    }
    return String.join("", groups);
    }
}


A: In your encodeCyclic function, you are adding a substring with the starting index i and the ending index i+3. However, if i+3 is equal or larger than the length of your string, it will throw an IndexOutOfBoundsException.
Here is the corrected version of your function:
public String encodeCyclic(String s) {
    List<String> groups = new ArrayList<>();
    for(int i = 0; i < s.length(); i += 3) {
        groups.add(s.substring(i, Math.min(i + 3, s.length())));
    }
    for(int i = 0; i < groups.size(); i++) {
        if(groups.get(i).length() == 3) {
            groups.set(i, groups.get(i).substring(1) + groups.get(i).charAt(0));
        }
    }
    return String.join("", groups);
}

The decodeCyclic function is almost correct, but the last character of each group should be the first one instead of the last. Here is the corrected version of your decodeCyclic function:
public String decodeCyclic(String s) {
    List<String> groups = new ArrayList<>();
    for(int i = 0; i < s.length(); i += 3) {
        groups.add(s.substring(i, Math.min(i + 3, s.length())));
    }
    for(int i = 0; i < groups.size();