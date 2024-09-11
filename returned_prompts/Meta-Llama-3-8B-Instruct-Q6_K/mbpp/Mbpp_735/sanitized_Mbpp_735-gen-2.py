def toggle_middle_bits(n):
    return (n & 1) | ((n & (~1) & ~(-1)) >> 1) | ((n & (~1) & -1) << 1) | (-1 & ~1)  # 1s before the last bit and after the first bit
    # equivalent to: (n^(n>>1)&~(-1))^(n<<1)&~1  # 1s before the last bit and after the first bit