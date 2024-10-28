    List<String> list = new ArrayList<String>();
    StringBuilder sb = new StringBuilder();
    for(int i = 0; i < paren_string.length(); i++) {
        char c = paren_string.charAt(i);
        if(c == '(') {
            sb.append(c);
        } else if(c == ')') {
            if(sb.length() == 0) {
                continue A;
            } else {
                int count = 1;
                while(count != 0) {
                    if(paren_string.charAt(i + count) == '(') {
                        count++;
                    } else if(paren_string.charAt(i + count) == ')') {
                        count--;
                    }
                }
                String str = paren_string.substring(i, i + count + 1);
                if(str.length() == count + 1 && isBalanced(str)) {
                    list.add(str);
                }
                i += count;
                sb = new StringBuilder();
            }
        }
    }
    return list;
}

public boolean isBalanced(String str) {
    int count = 0;
    for(int i = 0; i < str.length(); i++) {
        char c = str.charAt(i);
        if(c == '(') {
            count++;
        } else if(c == ')') {
            count--;
        }
        if(count < 0) {
            return false;
        }
    }
    return count == 0;
}
    }

































```