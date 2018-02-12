
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Description:

The following is a project that tries to detect the description for a Movie/TV Show from a random urls that contain them, using simple NLP techniques and web scraping.
It uses a small corpus of descriptions of movie/tv shows from different websites and uses this train the model.
Then it creates scores for how similar each description is to to different texts in the HTML. Finally, it uses these scores to sum and find the most probable description.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Things you need:

Python 3 and above and a few libraries:

    1) genism
    2) urllib3
    3) bs4
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
How to run the project:

Run the main.py file, that should be able to get the descriptions.

Also you can change the urls you want to test in the getWebData.py. You can modify the list urls to add or delete any urls you want to test on
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------