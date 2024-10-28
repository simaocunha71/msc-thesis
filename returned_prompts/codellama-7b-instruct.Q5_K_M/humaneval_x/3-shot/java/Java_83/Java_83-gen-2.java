        int count = 0;
        for (int i = 1; i <= n; i++) {
            String num = String.valueOf(i);
            if (num.startsWith("1") || num.endsWith("1")) count++;
        }
        return count;
    }
}

