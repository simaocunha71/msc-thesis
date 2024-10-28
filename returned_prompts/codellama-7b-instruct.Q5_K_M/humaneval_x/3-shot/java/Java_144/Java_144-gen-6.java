        String[] x_num_denom = x.split("/");
        String[] n_num_denom = n.split("/");
        int x_num = Integer.parseInt(x_num_denom[0]);
        int x_denom = Integer.parseInt(x_num_denom[1]);
        int n_num = Integer.parseInt(n_num_denom[0]);
        int n_denom = Integer.parseInt(n_num_denom[1]);

        if (x_num * n_denom == x_denom * n_num) return true;
        return false;
    }
}

