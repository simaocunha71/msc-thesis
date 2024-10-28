        int result = 0;
        for (int i = 0; i < lst.size(); i++) {
            int value = lst.get(i);
            if (i % 3 == 0) {
                value = value * value;
            } else if (i % 3 != 0 && i % 4 == 0) {
                value = value * value * value;
            }
            result += value;
        }
        return result;
    }
}

