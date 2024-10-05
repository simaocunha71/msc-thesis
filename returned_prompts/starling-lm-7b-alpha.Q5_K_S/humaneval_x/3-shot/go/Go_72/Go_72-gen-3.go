    return len(q) == 0 || (len(q) % 2 == 0 && q[0] + q[len(q) - 1] <= w && WillItFly(q[1 : len(q) - 1], w))
}



