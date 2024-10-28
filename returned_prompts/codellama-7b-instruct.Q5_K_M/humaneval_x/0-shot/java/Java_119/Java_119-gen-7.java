        for (int i = 0; i < lst.size(); i++) {
            String s = lst.get(i);
            if (s.contains("()") || s.contains("(") || s.contains(")")) {
                lst.remove(i);
                i--;
                continue A;
            }
        }
        return lst.size() > 0 ? "Yes" : "No";
    }
}