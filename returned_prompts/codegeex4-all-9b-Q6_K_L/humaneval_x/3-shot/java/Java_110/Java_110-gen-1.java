        boolean has_odd = false;
        for (int i = 0; i < lst1.size(); i++) {
            if (lst1.get(i) % 2 != 0) {
                has_odd = true;
            }
        }

        for (int i = 0; i < lst2.size(); i++) {
            if (lst2.get(i) % 2 == 0) {
                return "YES";
            }
        }
        return has_odd ? "NO" : "YES";
    }
}

