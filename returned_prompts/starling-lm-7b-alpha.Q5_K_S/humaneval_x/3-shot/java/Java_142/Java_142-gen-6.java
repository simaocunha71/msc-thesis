        for (int i = 0; i < lst.size(); i++) {
            if (i % 3 == 0) lst.set(i, lst.get(i) * lst.get(i));
            if (i % 4 == 0 && i % 3 != 0) lst.set(i, lst.get(i) * lst.get(i) * lst.get(i));
        }
        int result = 0;
        for (int i : lst) result += i;
        return result;
    }
}

