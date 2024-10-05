        String[] xArr = x.split("/");
        String[] nArr = n.split("/");

        int numX = Integer.parseInt(xArr[0]);
        int denX = Integer.parseInt(xArr[1]);

        int numN = Integer.parseInt(nArr[0]);
        int denN = Integer.parseInt(nArr[1]);

        if(numX * denN == numN * denX) {
            return true;
        }
        return false;
    }
}

The code takes two fractions as input, splits them into numerators and denominators and then checks if multiplication of numerators of two fractions equals to multiplication of denominators. If it is true, it returns true otherwise false.

*/

// Q2
/*

