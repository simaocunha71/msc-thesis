        int X = (Integer)x;
        int Y = (Integer)y;
        int Z = (Integer)z;
        return X == Y + Z || Y == X + Z || Z == X + Y;
    }
}

