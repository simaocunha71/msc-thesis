        String xStr = String.valueOf(x);
        int length = xStr.length();
        shift %= length;
        return xStr.substring(length - shift) + xStr.substring(0, length - shift);
     }
}

