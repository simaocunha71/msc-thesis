        int[] a = new int[k];
        int[] b = new int[k];

        // initialize the arrays
        for (int i = 0; i < a.length; i++) {
            a[i] = arr.get(i);
        }

        int sum = 0;

        // find the sum
        for (int i = 0; i < a.length; i++) {
            sum += a[i];
        }

        return sum;
    }
}


