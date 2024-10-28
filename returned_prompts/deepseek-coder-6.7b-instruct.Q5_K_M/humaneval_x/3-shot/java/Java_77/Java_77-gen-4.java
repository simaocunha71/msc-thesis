        int x = 0;

        while  (x * x * x < Math.abs(a)) {
            x++;
        }

        return  (x * x * x == Math.abs(a));
    }
}

