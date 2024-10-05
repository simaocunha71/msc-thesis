        String[] fruits = s.split(" ");
        int apples = Integer.parseInt(fruits[0].replace("apples", ""));
        int oranges = Integer.parseInt(fruits[1].replace("oranges", ""));
        return n - apples - oranges;
    }
}

