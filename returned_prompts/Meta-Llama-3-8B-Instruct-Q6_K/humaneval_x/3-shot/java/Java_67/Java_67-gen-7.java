        String[] parts = s.split(" ");
        int oranges = Integer.parseInt(parts[parts.length - 2].split(" ")[1]);
        int apples = Integer.parseInt(parts[parts.length - 1].split(" ")[0]);
        return n - apples - oranges;
    }
}

