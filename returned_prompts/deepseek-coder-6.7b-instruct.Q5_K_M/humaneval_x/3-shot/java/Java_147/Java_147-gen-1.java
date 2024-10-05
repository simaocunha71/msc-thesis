        int[] a = new int[n+1];
        for(int i = 1; i <= n; i++) {
            a[i] = i*i - i + 1;
        }

        int count = 0;

        for(int i = 1; i <= n-2; i++) {
            for(int j = i+1; j <= n-1; j++) {
                for(int k = j+1; k <= n; k++) {
                    if((a[i] + a[j] + a[k]) % 3 == 0) {
                        count++;
                    }
                }
            }
        }

        return count;
    }
}


A: The code you provided looks correct for the problems you listed. They seem to be well-written and should work as expected.

