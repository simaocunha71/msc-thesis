        String xString = Integer.toString(x);
        shift %= xString.length();

        return xString.substring(xString.length() - shift) + xString.substring(0, xString.length() - shift);
    }
}

