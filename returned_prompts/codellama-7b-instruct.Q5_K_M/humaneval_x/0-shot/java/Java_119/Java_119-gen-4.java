        // your solution goes here
        // return "Yes" or "No"
        int l = lst.size();
        if (l != 2) {
            return "No";
        }
        String s = lst.get(0);
        String t = lst.get(1);
        Stack<Character> st = new Stack<Character>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                st.push(c);
            } else {
                if (st.empty()) {
                    return "No";
                }
                st.pop();
            }
        }
        if (st.empty()) {
            st = new Stack<Character>();
            for (int i = 0; i < t.length(); i++) {
                char c = t.charAt(i);
                if (c == ')') {
                    st.push(c);
                } else {
                    if (st.empty()) {
                        return "No";
                    }
                    st.pop();
                }
            }
            if (st.empty()) {
                return "Yes";
            }
        }
        return "No";
    }
}
