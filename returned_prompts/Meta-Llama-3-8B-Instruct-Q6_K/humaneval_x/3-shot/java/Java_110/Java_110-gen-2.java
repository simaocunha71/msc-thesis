        int even_count = 0;
        for (int num : lst1) {
            if (num % 2 == 0) even_count++;
        }
        if (even_count == lst1.size()) return "YES";
        for (int i = 0; i < lst1.size(); i++) {
            for (int j = 0; j < lst2.size(); j++) {
                if (lst1.get(i) % 2 != 0 && lst2.get(j) % 2 == 0) {
                    lst1.set(i, lst2.get(j));
                    lst2.set(j, lst1.get(i));
                    if (isEven(lst1)) return "YES";
                    lst1.set(i, lst2.get(j));
                    lst2.set(j, lst1.get(i));
                }
            }
        }
        return "NO";
    }

    private boolean isEven(List<Integer> lst) {
        for (int num : lst) {
            if (num % 2 != 0) return false;
        }
        return true;
    }
}

