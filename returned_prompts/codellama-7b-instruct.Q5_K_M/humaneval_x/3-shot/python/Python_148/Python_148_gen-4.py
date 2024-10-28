    if planet1 in ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'):
        if planet2 in ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'):
            if planet1 == 'Mercury':
                if planet2 == 'Mercury':
                    return ()
                if planet2 == 'Venus':
                    return ('Venus',)
                if planet2 == 'Earth':
                    return ('Venus', 'Earth')
                if planet2 == 'Mars':
                    return ('Venus', 'Earth', 'Mars')
                if planet2 == 'Jupiter':
                    return ('Venus', 'Earth', 'Mars', 'Jupiter')
                if planet2 == 'Saturn':
                    return ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
                if planet2 == 'Uranus':
                    return ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus')
                if planet2 == 'Neptune':
                    return ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
            elif planet2 == 'Venus':
                if planet1 == 'Mercury':
                    return ('Venus',)
                if planet1 == 'Venus':
                    return ('Venus',)
                if planet1 == 'Earth':
                    return ('Venus', 'Earth')
                if planet1 == 'Mars':
                    return ('Venus', 'Earth', 'Mars')
                if planet1 == 'Jupiter':
                    return ('Venus', 'Earth', 'Mars', 'Jupiter')
                if planet1 == 'Saturn':
                    return ('Venus', 'Earth', 'Mars', '