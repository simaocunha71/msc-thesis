        for (int i = 0; i < lst.size(); i++) {
            String s = lst.get(i);
            String s2 = lst.get(i + 1);
            if (s.equals("(") && s2.equals(")")) {
                lst.remove(i);
                lst.remove(i);
                i--;
            }
        }
        if (lst.size() == 1 && lst.get(0).equals("")) {
            return "Yes";
        } else {
            return "No";
        }
    }
}
