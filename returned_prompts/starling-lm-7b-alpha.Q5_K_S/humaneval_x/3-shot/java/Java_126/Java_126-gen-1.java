        int length = lst.size();
        for (int i = 0; i < length - 1; i++) {
            if (lst.get(i) > lst.get(i + 1)) return false;
        }
        return true;
    }
}

