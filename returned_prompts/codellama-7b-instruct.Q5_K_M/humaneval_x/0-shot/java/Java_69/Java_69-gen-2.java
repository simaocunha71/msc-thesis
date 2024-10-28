        for (int i = 0; i < lst.size(); i++) {
            int count = 0;
            int value = lst.get(i);
            for (int j = 0; j < lst.size(); j++) {
                if (lst.get(j) == value) {
                    count++;
                }
            }
            if (count >= value) {
                return value;
            }
        }
        return -1;
    }
}

