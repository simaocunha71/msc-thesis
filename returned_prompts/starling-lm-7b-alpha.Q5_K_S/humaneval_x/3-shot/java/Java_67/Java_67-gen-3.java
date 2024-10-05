        String[] parts = s.split(" ");
        int apples = Integer.parseInt(parts[0].replace("apples", ""));
        int oranges = Integer.parseInt(parts[1].replace("oranges", ""));
        return n - apples - oranges;
    }
}

