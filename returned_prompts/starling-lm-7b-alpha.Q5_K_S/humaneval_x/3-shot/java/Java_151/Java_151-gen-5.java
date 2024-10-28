        int result = 0;
        for (Object obj : lst) {
            int number = (int) obj;
            if (number < 0 || number % 1.0 != 0) continue;
            result += number * number;
        }
        return result;
    }
}

