        int result = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (i % 3 == 0) {
                lst.set(i, lst.get(i) * lst.get(i));
            } else if (i % 3 == 2 && i % 4 != 0) {
                lst.set(i, lst.get(i) * lst.get(i) * lst.get(i));
            }
            result += lst.get(i);
        }
        return result;
    }
}

