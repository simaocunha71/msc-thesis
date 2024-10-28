        String[] numbers = new String[n + 1];

        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = String.valueOf(i);
        }

        return String.join(" ", numbers);
    }
}

