    var (
        xint, yint, zint int
        xok, yok, zok    bool
    )

    if xint, xok = x.(int); !xok {
        return false
    }
    if yint, yok = y.(int); !yok {
        return false
    }
    if zint, zok = z.(int); !zok {
        return false
    }

    return xint+yint == zint || yint+zint == xint || zint+xint == yint
}



