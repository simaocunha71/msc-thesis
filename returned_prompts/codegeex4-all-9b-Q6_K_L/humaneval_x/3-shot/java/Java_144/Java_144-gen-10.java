        int xnum = Integer.parseInt(x.split("/")[0]);
        int xdenom = Integer.parseInt(x.split("/")[1]);
        int nnum = Integer.parseInt(n.split("/")[0]);
        int ndenom = Integer.parseInt(n.split("/")[1]);

        if (xnum * ndenom == xdenom * nnum) return true;
        else return false;
    }
}

