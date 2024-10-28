        int result = 0;
        for (int i = 0; i < lst.size(); i++) {
            int entry = lst.get(i);
            if (i % 3 == 0) {
                result += entry * entry * entry;
            } else if (i % 4 == 0) {
                result += entry * entry;
            } else {
                result += entry;
            }
        }
        return result;
    }
}

