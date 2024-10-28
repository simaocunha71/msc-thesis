        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) > 0) {
                int val = lst.get(i);
                int count = 0;
                for (int j = 0; j < lst.size(); j++) {
                    if (lst.get(j) == val) {
                        count++;
                        if (count >= val) {
                            return val;
                        }
                    }
                }
            }
        }
        return -1;
    }
}
