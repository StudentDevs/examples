from bottle import route, run, request, redirect
from datetime import datetime, timedelta


@route('/')
def index():
    """Insecurely reflect user input back to the browser.
    """
    error = request.query.get('error', default='')

    return """<html>
    <head>
    </head>
    <body>

    <div>{error}</div>

    <h1>Enter a number of days in the future and we'll show the date.</h1>

    <form action=/show method=get>
    <input type=text name=days_in_future>
    <submit>
    </body>
    </html>""".format(error=error)


@route('/show')
def show():
    try:
        days_in_future = request.query.get('days_in_future', type=int)
        futuredate = datetime.utcnow() + timedelta(days=days_in_future)
    except Exception as exc:
        redirect('/?error={}'.format(exc))
        return

    return """<html>
    <head>
    </head>
    <body>
    {futuredate}
    <submit>
    </body>
    </html>""".format(futuredate=futuredate)


if __name__ == '__main__':
    run(host='0.0.0.0', port=80, server='paste')
