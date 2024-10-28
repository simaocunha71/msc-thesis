        if(n == 1)
            return 1;
        else
            return (int) Math.pow(10, n-1) + 2 * startsOneEnds(n-1);
    }
}

