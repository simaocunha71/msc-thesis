        String[] parts = s.split(" ");
        int orange = Integer.parseInt(parts[parts.length - 2].replace("oranges", "").replace("orange", "").trim());
        int apple = Integer.parseInt(parts[parts.length - 1].replace("apples", "").replace("apple", "").trim());
        return n - apple - orange;
    }
}

