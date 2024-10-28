        List<String> paren_groups = new ArrayList<>();
        int i = 0;
        while(i < paren_string.length()) {
            if(paren_string.charAt(i) == '(') {
                int j = 1;
                while(j < paren_string.length()) {
                    if(paren_string.charAt(j) == '(') {
                        j++;
                    }
                    else if(paren_string.charAt(j) == ')') {
                        j++;
                        break;
                    }
                    else {
                        j++;
                    }
                }
                paren_groups.add(paren_string.substring(i, j));
                i = j;
            }
            else {
                i++;
            }
        }
        return paren_groups;
    }
}
