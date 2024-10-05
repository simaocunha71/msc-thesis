        int result = -1;
        int mid = (x + y) / 2;

        if (mid % 2 == 0 && x <= mid && mid <= y) result = mid;

        if (result == -1) {
            if (x < mid && mid < y) {
                result = chooseNum(x, mid - 1);
            } else if (x > mid && mid > y) {
                result = chooseNum(mid + 1, y);
            }
        }
        return result;

    }
}

