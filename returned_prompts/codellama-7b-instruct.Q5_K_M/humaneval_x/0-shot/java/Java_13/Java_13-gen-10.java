        if(a<b){
            return greatestCommonDivisor(b, a);
        }
        if(a%b==0){
            return b;
        }
        return greatestCommonDivisor(a%b, b);
    }

    /**
    Return a greatest common divisor of two integers a and b
    >>> greatestCommonDivisor(3, 5)
    1
    >>> greatestCommonDivisor(25, 15)
    5
     */
    public int greatestCommonDivisor2(int a, int b) {
        // write your code here
        if(a<b){
            return greatestCommonDivisor2(b, a);
        }
        if(a%b==0){
            return b;
        }
        return greatestCommonDivisor2(a%b, b);
    }
}





