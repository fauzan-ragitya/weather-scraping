# Weather Webscraping

Personal webscraper project of historical climate data on various Singapore stations. 

Source: http://www.weather.gov.sg/climate-historical-daily/


## Description

There are approximately 63 stations available from the website. It presents data like temperature, rainfall and humidity level, and also wind speed across all stations.

## Getting Started

### Dependencies

Selenium is being used as the scraping library. Development was made on Windows environment

### Installing

Execute `pip install -r requirements.txt`

### Executing program

After installing the dependencies, you should be able to run the program by executing:
```
python main.py {month} {year}
```
Notes:
- `month` is the desired month (January,February,March,...,December)
- `year` is the desired year (2015,2016,...)
Generally, the website offers the data for the last 10 years. However, some stations may differ regarding the completeness of the data.

After executing the command, a Chrome window will pop up and start to crawl the data in specified {month} {year} accross all stations. Then, it would aggregate it and save it to local CSV file formatted as `{month}_{year}_data.csv`

