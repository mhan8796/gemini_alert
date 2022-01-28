# Gemini_alert
A take home assessment for Gemini

## Any necessary instructions for running your script
It can be ran with/without a command line argument
```
pip install -r requirements.txt
python3 apiAlerts.py
python3 apiAlerts.py -h
python3 apiAlerts.py -c btcusd -d 10
python3 apiAlerts.py -c ethusd -d 15
```

## Any dependencies that need to be met
The dependency file is requirements.txt

## Optional: A dockerfile to run the script
I had a dockerfile but the environment was diffcult to setup. I am using a windows machine. It requires to enable virtualization and hypervisor. The dockerfile is not uploaded because it was tested.

## What you would do next to further improve it
I could implement a function to first tell user all of the existing symbols. Currently, users may not know the available symbol input.


## Other interesting checks you might implement to alert on market behaviour
I could implement a linear regressiong perdiction on the future data based on the existing data. Something like this https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html.

## Your approach to solving the task, and any issues you faced with implementation
Could not understand the requirements after reading it. However the sample output helped greatly. At the beginning, I was not sure where to get the data. I thought the code could generate the random data. Then I browesed the public API and found the data. It would be very helpful to explicly say that the data will be obtained from the API. Also, for the DEBUG level I am not sure how it is being used. The script was called in CLI and I am not sure what behavior could trigger the DEBUG. I didn't implement DEBUG. It would be very helpful to include an example of how a DEBUG is used. For the rest of the project, I am just following the sample output to implement.

## The time it took you to write it
It took me less than one hour to write the code. However, reading and understanding the requirements, finding API, setting up the environment, and writing the Readme file took another hour.
