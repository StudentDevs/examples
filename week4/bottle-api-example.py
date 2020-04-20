from bottle import route, run, request, abort


@route('/')
def interest():
    """Calculates compound interest.

    https://en.wikipedia.org/wiki/Compound_interest
    """
    p = float(request.query.get('p', default=0))
    r = float(request.query.get('r', default=0))
    t = int(request.query.get('t', default=0))
    n = int(request.query.get('n', default=1))

    if not p or not r or not t:
        abort(400, 'required params: p (principle), r (nominal rate), '
                   't (time), n (compounding frequency)')

    future_value = p * (1 + r / n) ** (n * t)

    return {
        'p': p,
        'r': r,
        't': t,
        'n': n,
        'future_value': round(future_value, 2),
        'interest': round(future_value - p, 2),
    }


if __name__ == '__main__':
    run(host='0.0.0.0', port=80, server='paste')
