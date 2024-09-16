
def extract_even(nested_mixed_tuple):
    return tuple(
        (
            (
                extract_even(item) if isinstance(item, tuple) else item
                for item in subtuple
            )
            for subtuple in nested_mixed_tuple
        )
    )


