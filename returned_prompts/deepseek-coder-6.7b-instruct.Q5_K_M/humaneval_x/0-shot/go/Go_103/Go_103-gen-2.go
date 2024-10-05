    if n > m {
        return -1
    }
B:
    avg := math.Round(float64(n+m) / 2)
C:
    return fmt.Sprintf("%b", int(avg))
}

