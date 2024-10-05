        for (int i = 0; i < l.size() - 1; i++) {
            for (int j = i + 1; j < l.size(); j++) {
                for (int k = j + 1; k < l.size(); k++) {
                    if (l.get(i) + l.get(j) + l.get(k) == 0) return true;
                }
            }
        }
        return false;
    }
}

