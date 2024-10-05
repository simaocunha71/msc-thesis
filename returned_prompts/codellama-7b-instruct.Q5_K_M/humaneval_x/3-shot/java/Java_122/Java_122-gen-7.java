        int result = 0;
        int index = 0;

        while (index < k) {
            int number = arr.get(index);
            if (number < 10) {
                result += number;
                index++;
            } else {
                result += number % 10;
                index++;
            }
        }
        return result;
    }
}

