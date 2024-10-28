def convert(z):
    polar = complex(z).polar()
    return polar[0], polar[1]