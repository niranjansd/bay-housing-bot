# SF Bay Area Housing Twitter Bot

[@SFBayHousingBot](https://twitter.com/SFBayHousingBot) is a Twitter Bot that Tweets real estate listing in the SF Bay Area daily.
The information for this bot is scraped from Redfin and then formatted into tweets by CHATGPT3.5.

There are two versions of this code sample in this repository:

- [local.py](https://github.com/niranjansd/bay-housing-bot/blob/main/local.py) - The Python code sample for testing locally
- [gcp_function.py](https://github.com/niranjansd/bay-housing-bot/blob/main/gcp_function.py) - The version of the code deployed to [Cloud Functions](https://cloud.google.com/functions). 

#ToDo
The project is WIP currently with the following roadmap -
- Deploy to Cloud Functions
- Setup Cloud Scheduler
- Setup pictures.

## License

Licensed under the Apache License, Version 2.0: https://www.apache.org/licenses/LICENSE-2.0
