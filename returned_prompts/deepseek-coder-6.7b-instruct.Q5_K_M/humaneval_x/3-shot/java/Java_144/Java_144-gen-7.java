        String[] x_parts 
            = x.split("/");
        String[] n_parts 
            = n.split("/");

        double x_value 
            = Double.parseDouble(x_parts[0]) 
            / Double.parseDouble(x_parts[1]);
        double n_value 
            = Double.parseDouble(n_parts[0]) 
            / Double.parseDouble(n_parts[1]);

        return x_value * n_value == (int)(x_value * n_value);
     }
}

