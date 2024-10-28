        String[] parts = s.split(" ");
        int appleCount = 0;
        int orangeCount = 0;

        for (String part : parts) {
            if (part.startsWith("apples")) {
                appleCount = Integer.parseInt(part.replaceAll("apples", "").trim());
            } else if (part.startsWith("oranges")) {
                orangeCount = Integer.parseInt(part.replaceAll("oranges", "").trim());
            }
        }

        return n - appleCount - orangeCount;
    }
}