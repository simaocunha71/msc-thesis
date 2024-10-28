        int result = 0;
        for (Object obj : lst) {
            if (obj instanceof Integer) {
                Integer number = (Integer) obj;
                if (number % 2 == 1) {
                    result += number * number;
                }
            }
        }
        return result;
    }
}

