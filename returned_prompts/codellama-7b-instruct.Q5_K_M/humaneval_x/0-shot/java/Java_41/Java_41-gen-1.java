        int total = 0;
        for (int i = 1; i <= n; i++)
            for (int j = i + 1; j <= n; j++)
                total++;

        return total;
    }
}