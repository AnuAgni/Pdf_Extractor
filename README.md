# Pdf_Extractor
Using various libraries and frameworks in python to extract pdf from given url. Major ones are BeautifulSoup, requests,urllib, FastAPI,uvicorn and streamlit. Requirments.txt contains all the installations needed for this project to work, it does not contain uvicorn, which I downloaded seprately.

pdf_scraper.py contains the code needed to scrape the pdf links from the given webpage. While a straightforward process itself, we have to make a few adjustments in the url which is passed through fastapi. We might also have to make some changes in urls scraped, this will differ for the url given by the user. I had chosen a certain url in the begninning and hence made changes specific to it. I used a csv file initially so that I can review the links easily, but did not need it in the end hence commented it.

main.py contains the FastAPI code. I have added the output image in repository.

frontend.py contains the frontend developed using streamlit. It shows the output to user as dataframe. The user can then easily copy the links and open/download the pdf files according to their need. I ahve added an output image in the repository to help visualise the output.

