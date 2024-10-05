        String result = Integer.toString(x);
        result = result.substring(shift) + result.substring(0, shift);
        return result;
    }
}

