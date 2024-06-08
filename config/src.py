from config.settings import SCRAPER, SLEEP
from tqdm import tqdm

def run():
    try:
        SLEEP()
        SCRAPER.set_pages()
        for i in tqdm(range(SCRAPER.pages -1)):
            SCRAPER.get_page_elements()
            SCRAPER.get_elements_data()
            SLEEP()
            SCRAPER.next_page()
        SCRAPER.quit()
    except:
        SCRAPER.quit()