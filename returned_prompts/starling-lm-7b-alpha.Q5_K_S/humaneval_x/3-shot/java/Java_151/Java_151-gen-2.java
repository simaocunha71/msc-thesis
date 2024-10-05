        int result = 0;
        for (Object obj : lst) {
            if (obj instanceof Integer) {
                int number = (Integer) obj;
                if (number > 0 && number % 2 == 1) {
                    result += number * number;
                }
            }
        }
        return result;
    }
}

