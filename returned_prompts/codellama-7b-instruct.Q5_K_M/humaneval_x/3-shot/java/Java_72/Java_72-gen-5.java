        if (q.size() == 0) return false;
        if (q.size() == 1) return true;

        if (q.get(0) == q.get(q.size() - 1)) {
            for (int i = 1; i < q.size() - 1; i++) {
                if (q.get(i) != q.get(q.size() - 1 - i)) return false;
            }
            return true;
        } else {
            return false;
        }
    }
}

