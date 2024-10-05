        String[] parts = s.split(" ");
        int apples = 0, oranges = 0;
        for (String part : parts) {
            if (part.endsWith("apples")) apples = Integer.parseInt(part.replace("apples", ""));
            if (part.endsWith("oranges")) oranges = Integer.parseInt(part.replace("oranges", ""));
        }
        return n - apples - oranges;
    }
}

