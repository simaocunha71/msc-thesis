        if (!x.getClass().isInstance(Integer.class) || !y.getClass().isInstance(Integer.class) || !z.getClass().isInstance(Integer.class)) return false;
        if (x.equals(y + z)) return true;
        return false;
    }
}

