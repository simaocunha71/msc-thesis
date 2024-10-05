        if(x.getClass() != Integer.class || y.getClass() != Integer.class || z.getClass() != Integer.class)
            return false;
        else
            return (((Integer)x + (Integer)y) == (Integer)z) || (((Integer)x + (Integer)z) == (Integer)y) || (((Integer)y + (Integer)z) == (Integer)x);
    }
}
