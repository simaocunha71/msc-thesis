        int start = 0;
        int end = a;

        while (start <= end) {
            int mid = (start + end) / 2;
            long pow = (long) Math.pow(mid, 3);

            if (pow == a) {
                return true;
            } else if (pow < a) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return false;
    }
}

