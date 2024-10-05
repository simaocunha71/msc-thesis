        int result = 0;
        for (char c : value.toCharArray())
            if (c >= 'A' && c <= 'Z') result++;
        return result;
    }
}

