        int x_num = Integer.parseInt(x.split("/")[0]);
        int x_den = Integer.parseInt(x.split("/")[1]);
        int n_num = Integer.parseInt(n.split("/")[0]);
        int n_den = Integer.parseInt(n.split("/")[1]);

        if (x_num * n_den % x_den * n_num == 0) return true;
        else return false;
    }
}

