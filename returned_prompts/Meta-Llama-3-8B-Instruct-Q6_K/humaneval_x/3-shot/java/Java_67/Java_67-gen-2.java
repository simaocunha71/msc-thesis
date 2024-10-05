        String[] parts = s.split(" ");
        int appleCount = Integer.parseInt(parts[1].split(" ")[0]);
        int orangeCount = Integer.parseInt(parts[3].split(" ")[0]);
        return n - appleCount - orangeCount;
    }
}

