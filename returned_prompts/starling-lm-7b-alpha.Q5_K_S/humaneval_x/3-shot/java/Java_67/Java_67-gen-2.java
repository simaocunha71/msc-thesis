        String[] parts = s.split(" ");
        int apples = Integer.parseInt(parts[0].split(" ")[1]);
        int oranges = Integer.parseInt(parts[1].split(" ")[0]);
        return n - apples - oranges;
    }
}

