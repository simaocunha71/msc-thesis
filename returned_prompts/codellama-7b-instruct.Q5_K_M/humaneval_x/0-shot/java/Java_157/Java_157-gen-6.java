        int max = 0;
        int min = 0;
        int mid = 0;
        int[] arr = new int[]{a, b, c};

        Arrays.sort(arr);
        max = arr[2];
        min = arr[0];
        mid = arr[1];
        if (max * max == min * min + mid * mid) {
            return true;
        } else {
            return false;
        }

    }
}










