def highest_Power_of_2(n):
    i = 0
    while 2 ** i <= n:
        i += 1
    return 2 ** (i - 1)

assert highest_Power_of_2(10) == 8
assert highest_Power_of_2(16) == 16
assert highest_Power_of_2(32) == 32
assert highest_Power_of_2(64) == 64
assert highest_Power_of_2(128) == 128
assert highest_Power_of_2(256) == 256
assert highest_Power_of_2(512) == 512
assert highest_Power_of_2(1024) == 1024
assert highest_Power_of_2(2048) == 2048
assert highest_Power_of_2(4096) == 4096
assert highest_Power_of_2(8192) == 8192
assert highest_Power_of_2(16384) == 16384
assert highest_Power_of_2(32768) == 32768
assert highest_Power_of_2(65536) == 65536
assert highest_Power_of_2(131072) == 131072
assert highest_Power_of_2(262144) == 262144
assert highest_Power_of_2(524288) == 524288
assert highest_Power_of_2(1048576) == 1048576
assert highest_Power_of_2(2097152) == 2097152
assert highest_Power_of_2(4194304) == 4194304
assert highest_Power_of_2(8388608) == 8388608
assert highest_Power_of_2(16777216) == 16777216
