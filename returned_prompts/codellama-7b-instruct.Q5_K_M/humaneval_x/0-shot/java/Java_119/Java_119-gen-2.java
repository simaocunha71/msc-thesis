        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.size(); j++) {
                if (i == j) continue;
                if (lst.get(i).length() != lst.get(j).length()) continue;
                if (lst.get(i).equals(lst.get(j))) continue;
                String a = lst.get(i);
                String b = lst.get(j);
                if (a.length() != b.length()) continue;
                if (a.length() == 0 || b.length() == 0) continue;
                if (a.charAt(0) == '(' && a.charAt(a.length() - 1) == ')')
                    continue;
                if (b.charAt(0) == '(' && b.charAt(b.length() - 1) == ')')
                    continue;
                if (a.charAt(0) == ')' && a.charAt(a.length() - 1) == '(')
                    continue;
                if (b.charAt(0) == ')' && b.charAt(b.length() - 1) == '(')
                    continue;
            }
        }
        return "Yes";
    }
}



