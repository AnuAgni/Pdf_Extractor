from fastapi import FastAPI
import pdf_scraper
app=FastAPI()
pdf_link_list=[]
@app.get("/pdf/{web_url:path}")
async def get_link(web_url:str):
    pdf_link_list=pdf_scraper.get_pdf_links(web_url)
    return pdf_link_list
    

