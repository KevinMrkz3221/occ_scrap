from config.settings import SCRAPER, SLEEP
from tqdm import tqdm

def run():
    SLEEP()
    SCRAPER.set_pages()
    for i in tqdm(range(1, SCRAPER.pages -1)):
        SCRAPER.get_page_elements()
        SCRAPER.get_elements_data()
        SLEEP()
        SCRAPER.next_page()
    SCRAPER.quit()