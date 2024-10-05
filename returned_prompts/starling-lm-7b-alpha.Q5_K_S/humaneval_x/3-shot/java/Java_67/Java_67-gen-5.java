        String[] numbers_string = s.split(" ");
        int apples = Integer.parseInt(numbers_string[0].replace("apples", ""));
        int oranges = Integer.parseInt(numbers_string[1].replace("oranges", ""));

        return n - apples - oranges;
    }
}

