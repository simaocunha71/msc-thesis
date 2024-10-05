        int x = 0;
        while  (x*x*x <= Math.abs(a))  {
            if  (x*x*x == Math.abs(a)) return true;
            x += 1;
        }
        return false;
    }
}

