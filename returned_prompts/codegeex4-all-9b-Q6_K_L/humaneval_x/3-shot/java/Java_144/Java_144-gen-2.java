        int x_num = Integer.parseInt(x.split("/")[0]);
        int x_den = Integer.parseInt(x.split("/")[1]);
        int n_num = Integer.parseInt(n.split("/")[0]);
        int n_den = Integer.parseInt(n.split("/")[1]);

        return (x_num * n_den) % x_den == 0 && (x_den * n_num) % n_den == 0;
    }
}

