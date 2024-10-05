        for (int i = 0; i < l.size(); i++) {
            for (int j = 0; j < l.size(); j++) {
                if (i == j) continue;
                if (l.get(i) + l.get(j) == 0) return true;
            }
        }
        return false;
    }
}

