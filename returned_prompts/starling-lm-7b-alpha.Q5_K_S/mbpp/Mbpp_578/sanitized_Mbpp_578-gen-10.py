def interleave_lists(*lists):
    return [item for sublist in zip(*lists) for item in sublist]