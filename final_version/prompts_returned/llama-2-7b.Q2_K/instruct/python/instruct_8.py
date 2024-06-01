Write a Python function that generates a set of candidates using a given generator function, with a fixed maximum size and optional variable size parameter. The function should create a set of candidates with a specified maximum size, and assert that the length of each candidate set is equal to the maximum size. The function should also write the candidates to a file for later use.

    Only return the code, don't include any other information,
    such as a preamble or suffix.
    """
    def generate_candidates(size=None, maxlen=10):
        if size is None:
            pass
        else:
            print 'max len of the candidate is %d' % (maxlen)
            size = int(size)

        # create a new list with n items.
        candidates_list = [random.sample(range(0, 10), size)]

        return candidates_list