        int a = n;
        int b = n;
        int count = 0;
        while (a != 0 && b != 0) {
            if (a > b) a--;
            else if (a < b) b--;
            else {
                a--;
                b--;
                count++;
            }
        }

        return count;
    }
}


