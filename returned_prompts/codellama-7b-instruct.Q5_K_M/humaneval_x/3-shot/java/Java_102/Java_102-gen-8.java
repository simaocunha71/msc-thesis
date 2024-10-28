        int mid = (x + y) / 2;
        if (mid % 2 == 0 && x <= mid && mid <= y) return mid;
        else if (mid < x) return chooseNum(mid + 1, y);
        else if (mid > y) return chooseNum(x, mid - 1);
        else return -1;
    }
}

