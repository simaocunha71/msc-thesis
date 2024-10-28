        int[] arr = new int[n+1];
        for (int i = 1; i <= n; i++)
            arr[i] = i * i - i + 1;

        int count = 0;
        for (int i = 1; i <= n-2; i++)
            for (int j = i+1; j <= n-1; j++)
                for (int k = j+1; k <= n; k++)
                    if ((arr[i] + arr[j] + arr[k]) % 3 == 0)
                        count++;

        return count;
    }
}

