        int xInt = (int) x;
        int yInt = (int) y;
        int zInt = (int) z;

        return (xInt == (yInt + zInt)) ||
               (yInt == (xInt + zInt)) ||
               (zInt == (xInt + yInt));
    }
}

