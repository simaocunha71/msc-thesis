def dict_filter(d, n):
    return {key: value for key, value in d.items() if value >= n}  # filter dictionary based on the given value
    # assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}  # test the function
    # assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},185)=={'Alden Cantrell': 180, 'Pierre Cox': 190}  # test the function
    # assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},100)=={}  # test the function
    # assert dict_filter({},170)=={}  # test the function
    # assert dict_filter({'Cierra Vega': 175},170)=={'Cierra Vega': 175}  # test the function
    # assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190,'Alden Cantrell': 170},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}  # test the function
    # assert dict_filter({'Cierra Vega': 175},180)=={}  # test the function
    # assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190,'Alden Cantrell': 170},180)=={'Alden Cantrell': 180, 'Pierre Cox': 190}  # test the function
    # assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190,'Alden Cantrell': 170},100)=={}  # test the function
    # assert dict_filter