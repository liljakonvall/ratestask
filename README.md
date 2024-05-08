# RateTask solution

## Usage
Pre-Requisits: Example database running locally.
Run
```bash
pip install -r requirements.txt
python main.py
```
Then execute a get request on the endpoint, for example

China to UK:
http://127.0.0.1:5000/get_avg_prices?origin_slug=china_main&destination_slug=uk_main&start_date=2016-01-01&end_date=2022-01-01

Port to port:
http://127.0.0.1:5000/get_avg_prices?origin_slug=CNGGZ&destination_slug=EETLL&start_date=2016-01-01&end_date=2017-01-01

Port to baltic region: 
http://127.0.0.1:5000/get_avg_prices?origin_slug=CNGGZ&destination_slug=baltic_main&start_date=2016-01-01&end_date=2017-01-01

China to port:
http://127.0.0.1:5000/get_avg_prices?origin_slug=china_main&destination_slug=EETLL&start_date=2016-01-01&end_date=2017-01-01

## Testing
Test main flask handler with mock persistence: 
```bash
python test_main.py
```
Test persistence layer (integration), against the provided test database:
```bash
python integration_test_persistence.py
```