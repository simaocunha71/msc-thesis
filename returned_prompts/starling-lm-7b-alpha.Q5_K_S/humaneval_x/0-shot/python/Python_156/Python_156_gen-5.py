    from typing import Dict, Union

    def int_to_mini_roman(number: int) -> str:
        assert 1 <= number <= 1000, 'Input must be a positive integer between 1 and 1000'

        num_to_roman = {
            1000: 'm',
            900: 'cm',
            500: 'd',
            400: 'cd',
            100: 'c',
            90: 'xc',
            50: 'l',
            40: 'xl',
            10: 'x',
            9: 'ix',
            5: 'v',
            4: 'iv',
            1: 'i'
        }

        roman = ''
        for num, symbol in num_to_roman.items():
            while num <= number:
                roman += symbol
                number -= num

        return roman

    return int_to_mini_roman

# Run tests
import doctest
doctest.testmod()


