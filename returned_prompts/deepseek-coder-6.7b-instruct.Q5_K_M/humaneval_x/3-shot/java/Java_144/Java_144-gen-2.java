        String[] xParts = x.split("/");
        String[] nParts = n.split("/");

        int xNumerator = Integer.parseInt(xParts[0]);
        int xDenominator = Integer.parseInt(xParts[1]);
        int nNumerator = Integer.parseInt(nParts[0]);
        int nDenominator = Integer.parseInt(nParts[1]);

        return (xNumerator * nDenominator) % (xDenominator * nNumerator) == 0;
     }
}

