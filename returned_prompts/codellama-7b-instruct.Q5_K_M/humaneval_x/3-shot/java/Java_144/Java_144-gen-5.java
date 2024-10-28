        int x_numer = Integer.parseInt(x.split("/")[0]);
        int x_denom = Integer.parseInt(x.split("/")[1]);
        int n_numer = Integer.parseInt(n.split("/")[0]);
        int n_denom = Integer.parseInt(n.split("/")[1]);

        if (x_numer * n_denom == x_denom * n_numer) return true;
        else return false;
    }
}

