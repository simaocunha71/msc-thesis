        String s = Integer.toString(x);
        return s.substring(s.length() - shift) + s.substring(0, s.length() - shift);
    }
}

