    if n > m:
        return -1

    avg = (n + m) // 2
    rounded_avg = round(avg)
    bin_avg = bin(rounded_avg)[2:]

    return "0b" + bin_avg.zfill(8)  # Assuming max 8-bit binary
# zfill(8) is used to fill the remaining bits with zeros


