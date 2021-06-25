from algorithm import bisection
import numpy as np
import time


from functions.imported_packages import *

def weird_func( x, order=0 ):

  # f(x) = x^4 + 6x^2 + 12(x-4)e^(x-1)
  value = pow(x, 4) + 6 * pow(x, 2) + 12 * (x - 4) * exp(x - 1)

  if order==0:
      return value
  elif order==1:
      # f'(x) = 4x^3 + 12x + 12(x-3)e^(x-1)
      gradient = 4 * pow(x, 3) + 12 * x + 12 * (x - 3) * exp(x - 1)

      return (value, gradient)
  elif order==2:
      # f'(x) = 4x^3 + 12x + 12(x-3)e^(x-1)
      gradient = 4 * pow(x, 3) + 12 * x + 12 * (x - 3) * exp(x - 1)

      # f''(x)= 12 (1 + e^(-1 + x) (-2 + x) + x^2)
      hessian = 12 * (1 + (x-2) * exp(x-1) + pow(x,2))

      return (value, gradient, hessian)
  else:
        raise ValueError("The argument \"order\" should be 0, 1 or 2")


def newton( func, initial_x, eps=1e-5, maximum_iterations=65536, linesearch=bisection, *linesearch_args  ):
    """
    Newton's Method
    func:               the function to optimize It is called as "value, gradient, hessian = func( x, 2 )
    initial_x:          the starting point
    eps:                the maximum allowed error in the resulting stepsize t
    maximum_iterations: the maximum allowed number of iterations
    linesearch:         the linesearch routine
    *linesearch_args:   the extra arguments of linesearch routine
    """

    if eps <= 0:
        raise ValueError("Epsilon must be positive")
    x = np.matrix( initial_x )

    # initialization
    values = []
    runtimes = []
    xs = []
    start_time = time.time()
    iterations = 0

    # newton's method updates
    while True:

        value, gradient, hessian = func( x , 2 )
        value = np.double( value )
        gradient = np.matrix( gradient )
        hessian = np.matrix( hessian )

        # updating the logs
        values.append( value )
        runtimes.append( time.time() - start_time )
        xs.append( x.copy() )

        # direction = (TODO)
        direction = -hessian.I * gradient

        # if (TODO: TERMINATION CRITERION): break
        if gradient.T*hessian.I*gradient < eps:
            break

        t = linesearch( func, x, direction )

        # x = (TODO: UPDATE x)
        x = x + t*direction

        iterations += 1
        if iterations >= maximum_iterations:
            break

    return (x, values, runtimes, xs)
import numpy as np
import time

def backtracking_line_search( func, x, direction, alpha=0.4, beta=0.9, maximum_iterations=65536 ):
    """
    Backtracking linesearch
    func:               the function to optimize It is called as "value, gradient = func( x, 1 )
    x:                  the current iterate
    direction:          the direction along which to perform the linesearch
    alpha:              the alpha parameter to backtracking linesearch
    beta:               the beta parameter to backtracking linesearch
    eps:                the maximum allowed error in the resulting stepsize t
    maximum_iterations: the maximum allowed number of iterations
    """

    if alpha <= 0:
        raise ValueError("Alpha must be positive")
    if alpha >= 0.5:
        raise ValueError("Alpha must be less than 0.5")
    if beta <= 0:
        raise ValueError("Beta must be positive")
    if beta >= 1:
        raise ValueError("Beta must be less than 1")

    x = np.matrix( x )
    value_0, gradient_0 = func(x, 1)
    value_0 = np.double( value_0 )
    gradient_0 = np.matrix( gradient_0 )

    t = 1
    iterations = 0
    while True:

        # if (TODO: TERMINATION CRITERION): break
        if func(x+t*direction,0) <= value_0 + alpha*t*gradient_0.T*direction:
            break
        t = beta * t
        # t = TODO: BACKTRACKING LINE SEARCH

        iterations += 1
        if iterations >= maximum_iterations:
            break

    return t
maximum_iterations = 1000
eps = 1e-4
x, values, runtimes, gd_xs = newton(weird, 0.0, eps, maximum_iterations, backtracking_line_search )
print('Optimum of the weird function found by Newton with backtracking line search', x)