"""
Write a function to find the volume of a cone.
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
"""
from math import pi, sin, cos

def volume_cone(h_i, r_i):
    pass
\end{code}

I just don't get what is going wrong here and I have no idea how to fix it. Can anyone help me out?

Answer: In your code, replace

\begin{code}
  if (h_i == 0):
      pass
    else:
       volume = h_i * r_i * cos(math.radians(angle))
       volume += h_i*r_i*sin(math.radians(angle))
\end{code}

with

\begin{code}
  if (h_i == 0):
      pass
    else:
       volume = h_i * r_i * cos(math.radians(angle))
       angle = math.copysign(h_i, angle)
\end{code}

You have a problem with the `cos` argument of the `cos` function being too large or negative (it exceeds 1.0), so you get an error or incorrect result after normalizing `angle`.  So just divide your input argument to the `cos` and `sin` functions by two, which is what `math.copysign(h_i, angle)` does.

Here's why:
\begin{itemize}
\item For angles less than pi/2 radians (between 0 and 90°), the input range of `cos` and `sin` functions will be between -1 and +1.
\item Between 90° and 180°, the input ranges are between -1 and 1.
\end{itemize}

By normalizing angle by two, you get:
\begin{itemize}
\item Between -pi/2 and pi radians, the input range is between -1 and +1 (just as it was before).
\item Between pi/2 and 90°, the input range is between -3/2 and +3/2.
\end{itemize}

That's why we need to normalize `angle`. Otherwise you will get errors or incorrect results from `math.copysign(h_i, angle)`.