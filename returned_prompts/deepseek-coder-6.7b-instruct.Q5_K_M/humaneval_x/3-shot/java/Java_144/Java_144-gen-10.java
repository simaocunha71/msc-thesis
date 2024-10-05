        String[] xFraction = x.split("/");
        String[] nFraction = n.split("/");

        int xNumerator = Integer.parseInt(xFraction[0]);
        int xDenominator = Integer.parseInt(xFraction[1]);
        int nNumerator = Integer.parseInt(nFraction[0]);
        int nDenominator = Integer.parseInt(nFraction[1]);

        return (xNumerator * nDenominator) % xDenominator == 0;
     }
}

