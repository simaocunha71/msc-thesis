        StringBuilder str = new StringBuilder(Integer.toString(x));

        if(shift > str.length()) {
            return str.reverse().toString();
        }

        StringBuilder shifted = new StringBuilder(str.substring(str.length() - shift));
        shifted.append(str.substring(0, str.length() - shift));
        return shifted.toString();
     }
}

