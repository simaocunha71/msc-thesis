        int n = lst.size();
        if (n < 2) return true;
        int last = lst.get(0);
        for (int i = 1; i < n; i++) {
            int curr = lst.get(i);
            if (curr < last) return false;
            if (curr == last) {
                lst.remove(i);
                n--;
                i--;
                continue A;
            }
            last = curr;
        }
        return true;
    }
}
