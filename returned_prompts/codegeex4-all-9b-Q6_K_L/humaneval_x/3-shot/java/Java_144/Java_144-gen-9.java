        int x_num = Integer.parseInt(x.split("/")[0]);
        int x_denom = Integer.parseInt(x.split("/")[1]);
        int n_num = Integer.parseInt(n.split("/")[0]);
        int n_denom = Integer.parseInt(n.split("/")[1]);

        return (x_num * n_denom) % x_denom == 0 && (x_denom * n_num) % n_denom == 0;
    }
}

