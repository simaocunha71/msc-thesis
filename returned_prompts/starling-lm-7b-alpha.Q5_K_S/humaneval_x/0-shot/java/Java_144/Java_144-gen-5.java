        int n1, n2, d1, d2;
        n1 = Integer.parseInt(x.split("/")[0]);
        d1 = Integer.parseInt(x.split("/")[1]);
        n2 = Integer.parseInt(n.split("/")[0]);
        d2 = Integer.parseInt(n.split("/")[1]);

        if (n1 * d2 == n2 * d1) {
            return true;
        } else {
            return false;
        }
    }
}









































```
