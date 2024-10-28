    if(a > 0 && b > 0 && c > 0){
        double s = (a + b + c) / 2;
        return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }else{
        throw new IllegalArgumentException("Lengths of side must be greater than 0.");
    }
    }

    /**
    Given two sides and high return area for a quadrilateral.
    >>> quadrilateralArea(3, 4)
    6
     */
   