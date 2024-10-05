        int result = 0;
        int i = 0;
        while (i < lst.size()) {
            if (lst.get(i) % 2 == 0) {
                result += lst.get(i);
                i += 2;
            } else {
                i += 1;
            }
        }
        return result;
    }
}

