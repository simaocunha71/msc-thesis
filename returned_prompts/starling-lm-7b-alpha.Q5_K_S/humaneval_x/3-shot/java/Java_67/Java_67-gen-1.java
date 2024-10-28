        String[] parts = s.split(" ");
        int apples = Integer.parseInt(parts[0].substring(3));
        int oranges = Integer.parseInt(parts[1].substring(0, parts[1].length() - 1));
        return n - apples - oranges;

    }
}

