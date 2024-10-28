        int result = 0;
        for (int i = 0; i < lst.size(); i++) {
            int number = lst.get(i);
            if (i % 3 == 0) {
                result += number * number;
            } else if (i % 4 == 0 && i % 3 != 0) {
                result += number * number * number;
            }
        }
        return result;
    }
}

