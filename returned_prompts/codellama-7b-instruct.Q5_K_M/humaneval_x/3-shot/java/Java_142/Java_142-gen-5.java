        int result = 0;

        for (int i = 0; i < lst.size(); i++) {
            int current_value = lst.get(i);
            if (i % 3 == 0) {
                result += current_value * current_value * current_value;
            } else if (i % 4 == 0) {
                result += current_value * current_value * current_value;
            } else {
                result += current_value;
            }
        }
        return result;
    }
}

