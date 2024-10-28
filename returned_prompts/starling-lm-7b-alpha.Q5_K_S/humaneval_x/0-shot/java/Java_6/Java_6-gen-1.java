    List<Integer> res = new ArrayList<>();
    int max_level = 0;
    int cur_level = 0;

    for(char c : paren_string.toCharArray()) {
        if(c=='(') {
            cur_level++;
            if(cur_level > max_level) max_level = cur_level;
        }
        else {
            cur_level--;
        }
    }
    res.add(max_level);
    while(paren_string.length() > 0) {
        paren_string = paren_string.substring(1);
        max_level = 0;
        cur_level = 0;
        for(char c : paren_string.toCharArray()) {
            if(c=='(') {
                cur_level++;
                if(cur_level > max_level) max_level = cur_level;
            }
            else {
                cur_level--;
            }
        }
        res.add(max_level);
    }
    return res;

    }
}


























































































































































































































































