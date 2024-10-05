        int result = 0;
        for (int i = 0; i < lst.size(); i++) {
            int value = lst.get(i);
            if (value % 2 == 0 && i % 2 == 0) {
                result += value;
            }
        }
        return result;
    }
}

