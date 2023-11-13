# Relations of Various Factors with the American Stock Market

## Study the relationship between the **American stock market, real estate, economy and gold prices**.

### Getting Stock Market Data

Extracted the **Russell 3000 Index** values for each month from **1st January 1990 until 10th October 2023** using the **TwelveData API** in JSON format.
The reason to take the Russel 3000 Index is because it takes into account a large number of stocks, thereby giving a better idea of the performance of the US stock market.

### Getting Real Estate Data

Downloaded data in CSV format on quarterly average sales price of houses sold in the United States from 01/01/1990 to 01/07/2023.  
Source => [Federal Reserve Economic Data](https://fred.stlouisfed.org/series/ASPUS)

### Getting GDP Data

Downloaded data in CSV format on the GDP in USD of the USA from 1990 to 2022.  
Source => [The World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=US)

### Getting Gold price data

Extracted gold price for every year from the year 1990 to 2022 in JSON format, using API from GoldAPI
