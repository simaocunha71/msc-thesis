    return int(math.Mod(float64(n), float64(p)))
}  // or return n % p
}  // or return int(New(big.Int).Mod(big.NewInt(int64(n)), big.NewInt(int64(p))).Int64())  // for big numbers



