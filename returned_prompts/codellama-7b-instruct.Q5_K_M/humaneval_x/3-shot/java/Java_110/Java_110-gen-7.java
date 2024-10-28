        for (int i = 0; i < lst2.size(); i++) {
            if (lst2.get(i) % 2 == 0) {
                lst1.add(lst2.remove(i));
                break;
            }
        }
        if (lst2.size() == 0) return "YES";
        else return "NO";
    }
}

