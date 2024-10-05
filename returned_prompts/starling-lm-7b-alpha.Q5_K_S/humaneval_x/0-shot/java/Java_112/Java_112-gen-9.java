    List<Object> res = new ArrayList<>();
    if(s.length() < c.length()) return res;
    StringBuilder sb = new StringBuilder();
    for(int i = 0; i < s.length(); i++) {
        boolean flag = true;
        for(int j = 0; j < c.length(); j++) {
            if(s.charAt(i) == c.charAt(j)) {
                flag = false;
                break;
            }
        }
        if(flag) sb.append(s.charAt(i));
    }
    String str = sb.toString();
    res.add(str);
    if(str.length() % 2 == 0) {
        boolean flag = true;
        for(int i = 0; i < str.length() / 2; i++) {
            if(str.charAt(i) != str.charAt(str.length() - i - 1)) {
                flag = false;
                break;
            }
        }
        if(flag) res.add(true);
        else res.add(false);
    }else {
        boolean flag = true;
        for(int i = 0; i < str.length() / 2; i++) {
            if(str.charAt(i) != str.charAt(str.length() - i - 1)) {
                flag = false;
                break;
            }
        }
        if(flag) res.add(true);
        else res.add(false);
    }
    return res;
    }
}
































```