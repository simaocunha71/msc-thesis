        int x_n = Integer.parseInt(x.split("/")[0]);
        int x_d = Integer.parseInt(x.split("/")[1]);
        int n_n = Integer.parseInt(n.split("/")[0]);
        int n_d = Integer.parseInt(n.split("/")[1]);

        if ((x_n * n_d) % (x_d * n_n) == 0) {
            return true;
        } else {
            return false;
        }
    }
}

