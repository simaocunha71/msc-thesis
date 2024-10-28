        if (txt.contains(" ")) return Arrays.asList(txt.split(" "));
        if (txt.contains(",")) return Arrays.asList(txt.split(","));
        int count = 0;
        for (char c : txt.toCharArray()) {
            if (c >= 'a' && c <= 'z' && (c - 'a') % 2 == 1) count += 1;
        }
        return count;
    }
}

