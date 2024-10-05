        if(n==1) return false;
        if(n==2) return true;
        if(n%2==0) return false;
        for(int i=3;i*i<=n;i+=2){
            if(n%i==0) return false;
        }
        return true;
    }

    /**
    Return the sum of two given integers.
    >>> add(1, 2)
    3
    >>> add(1, 0)
    1
    >>> add(-1, 0)
    -1
    >>> add(-1, -1)
    -2
    >>> add(-1, 1)
    -1
    >>> add(1, -1)
    0
    >>> add(0, 1)
    1
    >>> add(0, -1)
    -1
     */
    public int add(int a, int b) {
        return a+b;
    }

    /**
    Return the absolute difference between two given integers,
    that is, the difference between their absolute values.
    >>> absDiff(1, 2)
    1
    >>> absDiff(-1, 2)
    1
    >>> absDiff(-1, -2)
    2
    >>> absDiff(1, -2)
    2
    >>> absDiff(1000, -1000)
    2000
    >>> absDiff(-1000, 1000)
    2000
     */
    public int absDiff(int a, int b) {
        return Math.abs(a-b);
    }

    /**
    Return the product of two given integers.
    >>> multiply(1, 2)
    2
    >>> multiply(1, 0)
    0
    >>> multiply(-1, 0)
    0
    >>> multiply(-1, -2)
    2
    >>> multiply(-1, 1)
    -1
    >>> multiply(1, -1)
    -1
    >>> multiply(0, 1)
    0
    >>> multiply(0, -1)
    0
     */
    public int