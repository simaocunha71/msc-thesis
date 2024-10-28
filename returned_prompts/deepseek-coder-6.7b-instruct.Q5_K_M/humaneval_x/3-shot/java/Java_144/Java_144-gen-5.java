        String[] xSplit = x.split("/");
        String[] nSplit = n.split("/");
        int xNum = Integer.parseInt(xSplit[0]);
        int xDen = Integer.parseInt(xSplit[1]);
        int nNum = Integer.parseInt(nSplit[0]);
        int nDen = Integer.parseInt(nSplit[1]);

        return (xNum * nDen) == (nNum * xDen);
     }
}

