        for (int i = 0; i < lst.size(); i++) {
            int x = lst.get(i);
            if (x > 1) {
                int cnt = 1;
                for (int j = i + 1; j < lst.size(); j++) {
                    if (lst.get(j) == x) {
                        cnt++;
                    } else {
                        break;
                    }
                }
                if (cnt >= x) {
                    return x;
                }
            }
        }
        return -1;
    }
}
