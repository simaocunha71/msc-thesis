"""
Write a python function to set the left most unset bit.
assert set_left_most_unset_bit(10) == 14
"""
import sys;
from os import urandom, write;
def get_len(x):
    return (((urandom() ^ (x * 7)) & 85) + 1).bit_length();
if __name__=="__main__":
    while True:
        a = sys.argv[2] or "0"
        b = sys.argv[3] or "0"
        if (get_len(a)) != (get_len(b)):
            print("Incompatible lengths", file=sys.stderr)
        elif get_len(a) > 16:
            print("Too big", file=sys.stderr);
            break;
        else:
            w = write(b"");
            w.write(str(int(get_len(a))));
            w.write(' '+str((int)a));
            w.write(' '+str((int)b))
