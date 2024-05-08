from flask import Flask
from flask import request

from persistence import get_avg_prices

app = Flask(__name__)


@app.route('/get_avg_prices')
def get_avg_prices_api():
    # We can just pass request.args, but then it is unclear what the parameters are.
    query_parameters = {
        'origin_slug': request.args['origin_slug'],
        'destination_slug': request.args['destination_slug'],
        'start_date': request.args['start_date'],
        'end_date': request.args['end_date']
    }
    return get_avg_prices(query_parameters)


if __name__ == '__main__':
    app.run(debug=True)