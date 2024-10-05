        int count = 0;
        for (int i = 1; i < (int) Math.pow(10, n); i++) {
            String s = String.valueOf(i);
            if (s.startsWith("1") || s.endsWith("1")) count++;
        }
        return count;
    }
}

