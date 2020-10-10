# Automated-Prediction

## A simple [linear regression](https://en.wikipedia.org/wiki/Linear_regression#:~:text=In%20statistics%2C%20linear%20regression%20is,is%20called%20simple%20linear%20regression. "regression") model that lets you select a `Google Sheet` from the drive and calculates all the optimised parameters of the model using `Gradient_Descent_Algorithm` and lets you save all the parameters and evaluation metrics of the model to your `Google Drive.`

 1. ### It not just calculates the optimised parameters of your model but lets you graphically visualise the relationship between various other parameters.

 2. ### It lets you save files to your drive after your proper authentication.
```
You Come up  with a Dataset and walk out with the most optimised parameters of the model...Everything else(Data Preprocessing and Data Modelling) is taken care of.
```

### It's kind of a drag and drop model.

## How to install?
--------------------
```python
pip install dataVisualisation
```

## How to use:
----------------
1. ### import the module
2. ### call the main function using the module

```python
import dataVisualisation
dataVisualisation.main()
```

## Prerequisties required for the module to run successfully:
------------------------------------------------------------
#### Before you call the module make sure you have installed all the following modules
```python
pip install pydrive
pip install gspread
pip install pandas
pip install sklearn
pip install matplotlib
```
## Set-Up:
---------------------------
### Before you go ahead with running the module...there are a few steps that needs to be followed:
1. Create a  new project on [google cloud console](https://console.developers.google.com)
2. Activate the Google Drive API
3. Create [Credentials](https://cran.r-project.org/web/packages/gargle/vignettes/get-api-credentials.html) for the google drive API
4. Save the downloaded file as `credentials.json`
5. Share the desired google sheet with the client email in credentials.json file
6. Activate the google sheets API
7. Create [oAuth2 Client credentials](https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred) and save the file as `client_secrets.json`

## Usage and functionality:
-------------------------------
1. This module can be used with any of the non categorical dataset but make sure to have the target variable at the last column of the spreadsheet.
2. Make sure `client_secrets.json` and `credentials.json` is inside the same directory as the Python program.
3. The directory(path) should not contain any subdirectories inside it.
4. Make sure to share the google sheet to client_email from the drive.



## References:
------------------
1. [Creating a python library](https://python-packaging.readthedocs.io/en/latest/index.html "creating a library")
2. [Hosting the library on PyPI](https://medium.com/little-big-engineering/lets-talk-about-python-packaging-6d84b81f1bb5 "hosting the library")
3. [working with google sheets](https://www.youtube.com/watch?v=cnPlKLEGR7E&t=10s&ab_channel=TechWithTim "googleSheets")
4. [working with markdown Language](https://www.youtube.com/watch?v=bpdvNwvEeSE&ab_channel=HiteshChoudhary "markdownLanguage")

## To check the module on PyPI head on to [my PyPI account](https://pypi.org/project/dataVisualisation)

## License:
---------------------
This Package is distributed under the [MIT license](https://opensource.org/licenses/MIT)

