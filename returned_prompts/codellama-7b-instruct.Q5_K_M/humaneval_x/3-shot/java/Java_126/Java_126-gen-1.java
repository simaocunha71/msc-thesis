        int prev = lst.get(0);
        for (int i = 1; i < lst.size(); i++) {
            int curr = lst.get(i);
            if (prev > curr || curr == prev) return false;
            prev = curr;
        }
        return true;
    }
}

