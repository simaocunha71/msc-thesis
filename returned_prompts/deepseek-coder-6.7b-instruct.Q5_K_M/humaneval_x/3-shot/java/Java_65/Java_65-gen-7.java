        String x_str = String.valueOf(x);
        int length = x_str.length();

        if  (shift  %  length  == 0) return x_str;

        return x_str.substring(length - shift % length) + x_str.substring(0, length - shift % length);
     }
}

