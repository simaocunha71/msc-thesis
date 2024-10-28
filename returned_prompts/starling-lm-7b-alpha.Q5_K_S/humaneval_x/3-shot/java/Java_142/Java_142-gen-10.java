        int result = 0;
        for (int i = 0; i < lst.size(); i++) {
            int value = lst.get(i);
            if (i % 3 == 0) {
                result += value * value;
            } else if (i % 4 == 0 && i % 3 != 0) {
                result += value * value * value;
            }
        }
        return result;
    }
}

