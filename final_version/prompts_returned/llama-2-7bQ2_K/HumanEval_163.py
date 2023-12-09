
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    return list(range(a, b + 1, 2))
    

def main():
    a = sys.argv[1]
    b = int(sys.argv[2])

    print generate_integers(int(a), int(b)), "\n"

if __name__ == '__main__':
    main()