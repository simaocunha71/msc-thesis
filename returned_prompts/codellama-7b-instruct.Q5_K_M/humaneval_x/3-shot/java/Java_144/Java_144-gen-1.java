        String[] x_arr = x.split("/");
        String[] n_arr = n.split("/");

        int x_num = Integer.parseInt(x_arr[0]);
        int x_den = Integer.parseInt(x_arr[1]);

        int n_num = Integer.parseInt(n_arr[0]);
        int n_den = Integer.parseInt(n_arr[1]);

        if ((x_num * n_den == x_den * n_num) && (x_den * n_den != 0)) return true;
        else return false;
    }
}

