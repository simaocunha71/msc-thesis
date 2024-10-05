        int result = 0;
        for (Object obj : lst) {
            int number = (int) obj;
            if (number % 2 == 0 || number < 0) continue;
            result += number * number;
        }
        return result;
    }
}

