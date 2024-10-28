        for (int i = 0; i < l.size() - 1; i++) {
            if (l.get(i) == l.get(i + 1)) continue;
            if (l.get(i) > l.get(i + 1)) {
                for (int j = i + 1; j < l.size() - 1; j++) {
                    if (l.get(j) > l.get(j + 1)) continue;
                    else {
                        System.out.println("false");
                        return false;
                    }
                }
            } else {
                for (int j = i + 1; j < l.size() - 1; j++) {
                    if (l.get(j) < l.get(j + 1)) continue;
                    else {
                        System.out.println("false");
                        return false;
                    }
                }
            }
        }
        System.out.println("true");
        return true;
    }
}
