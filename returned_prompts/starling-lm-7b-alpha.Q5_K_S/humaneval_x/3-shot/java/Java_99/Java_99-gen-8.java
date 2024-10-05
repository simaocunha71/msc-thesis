        if (value.charAt(0) == '-') {
            return Math.max(-Integer.parseInt(value.substring(1)),
                            Integer.parseInt(value.substring(1)));
        } else {
            return Math.min(Integer.parseInt(value),
                            Integer.parseInt(value.substring(1)));
        }
    }
}

