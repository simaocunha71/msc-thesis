        String[] x_parts = x.split("/");
        String[] n_parts = n.split("/");

        int x_num = Integer.parseInt(x_parts[0]);
        int x_den = Integer.parseInt(x_parts[1]);

        int n_num = Integer.parseInt(n_parts[0]);
        int n_den = Integer.parseInt(n_parts[1]);

        return (x_num * n_den) % x_den == 0;
     }
}

