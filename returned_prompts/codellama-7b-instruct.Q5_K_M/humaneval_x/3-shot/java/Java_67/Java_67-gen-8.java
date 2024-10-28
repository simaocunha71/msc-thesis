        String[] fruits = s.split(" ");
        int apples = Integer.parseInt(fruits[0]);
        int oranges = Integer.parseInt(fruits[1]);
        return n - apples - oranges;
    }
}

