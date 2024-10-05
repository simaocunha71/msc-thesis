        if (txt.contains(" ")) return txt.split(" ");
        if (txt.contains(",")) return txt.split(",");
        int result = 0;
        for (char c : txt.toLowerCase().toCharArray()) {
            if ((c - 'a') % 2 == 1) result += 1;
        }
        return result;
    }
}

