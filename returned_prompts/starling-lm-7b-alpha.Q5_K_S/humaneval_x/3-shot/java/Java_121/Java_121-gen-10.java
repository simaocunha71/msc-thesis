        int result = 0;
        int index = 0;
        for (int number : lst) {
            if (index % 2 == 0 && number % 2 != 0) {
                result += number;
            }
            index += 1;
        }
        return result;
    }
}

