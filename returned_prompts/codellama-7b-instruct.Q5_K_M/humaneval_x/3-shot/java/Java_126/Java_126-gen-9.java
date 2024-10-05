        if (lst.size() <= 1) return true;

        Integer prev = lst.get(0);
        for (int i = 1; i < lst.size(); i++) {
            Integer curr = lst.get(i);
            if (curr < prev) return false;
            if (curr == prev) return false;
            prev = curr;
        }
        return true;
    }
}

