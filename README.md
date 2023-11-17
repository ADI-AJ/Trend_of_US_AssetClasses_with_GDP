# Relationship of various asset classes in the USA with it's GDP 

## Study the relationship between the **American stock market, real estate, economy and gold prices**.


### Getting Data

#### Stock Market Data

Extracted the **Russell 3000 Index** values for each month from **1st January 1990 until 10th October 2023** using the **TwelveData API** in JSON format.
The reason to take the Russel 3000 Index is because it takes into account a large number of stocks, thereby giving a better idea of the performance of the US stock market.

For cloud => 
[The JSON file could be pushed to **AWS S3** for storing using the **boto3** library (AWS SDK for Python)](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html) 

[The JSON file could be pushed to **Azure Blob** for storing using the **azure-storage-blob** library](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?tabs=managed-identity%2Croles-azure-portal%2Csign-in-azure-cli)

#### Real Estate Data

Downloaded data in CSV format on quarterly average sales price of houses sold in the United States from 01/01/1990 to 01/07/2023.  
Source => [Federal Reserve Economic Data](https://fred.stlouisfed.org/series/ASPUS)

For cloud => Can be stored in any **object storage** solutions such as **AWS S3** and **Azure Blob Storage**.

#### GDP Data

Downloaded data in CSV format on the GDP in USD of the USA from 1990 to 2022.  
Source => [The World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=US)

For cloud => Can be stored in any **object storage** solutions such as **AWS S3** and **Azure Blob Storage**.

#### Gold Price data

Extracted gold price for every year from the year 1990 to 2022 in JSON format, using API from GoldAPI

For cloud => 
[The JSON file could be pushed to **AWS S3** for storing using the **boto3** library (AWS SDK for Python)](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html) 

[The JSON file could be pushed to **Azure Blob** for storing using the **azure-storage-blob** library](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?tabs=managed-identity%2Croles-azure-portal%2Csign-in-azure-cli)
