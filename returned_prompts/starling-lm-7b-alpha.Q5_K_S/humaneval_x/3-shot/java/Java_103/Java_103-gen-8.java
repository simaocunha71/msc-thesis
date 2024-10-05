        if (n > m) return -1;
        int average = (n + m) / 2;
        String result = Integer.toBinaryString(average);
        while (result.length() < 8) result = "0" + result;
        return result;
    }
}

