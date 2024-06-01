from selenium.webdriver.common.by import By 
from selenium import webdriver


from models.vacante import Vacante



class Scrapper:
    def __init__(self, args, vacancyController, chrome_options, SLEEP) -> None:
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(args.url)
        self.vacancyController = vacancyController
        self.data = []
        self.SLEEP = SLEEP

    def set_filters(self):
        date_btn = self.driver.find_element(By.ID, "facetItem-TM")
        date_btn.click()
        today = self.driver.find_element(By.ID, "TM-0")
        today.click()
        self.SLEEP()
        self.driver.find_element(By.XPATH, '/html/body/main/div[2]/nav/form/div[3]/button').click()
        

    def get_page_elements(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="flex flex-col relative z-1 m-0 p-0 box-border mx-auto"]')
        return elements
    
    def get_vacancy_data(self, card):
        titulo = card.find_element(By.CSS_SELECTOR, 'div[class="flex justify-between items-start mt-2"] > p').text
        categorias = card.find_elements(By.CSS_SELECTOR, 'div[class="flex flex-col gap-2"] > div > a')
        categoria = categorias[0].text
        subcategoria = categorias[1].text
        try:
            educacion = card.find_element(By.XPATH, '/html/body/main/div[4]/div/div/div[8]/div[3]/span[2]').text
        except:
            educacion = 'NA'
        detalles = []
        try:
            detalles.append(card.find_element(By.XPATH, '/html/body/main/div[4]/div/div/div[10]/a').text)
        except:
            pass
        try:
            detalles.append(card.find_element(By.XPATH, '/html/body/main/div[4]/div/div/div[11]/a').text)
        except:
            pass
    
        try:
            detalles.append(card.find_element(By.XPATH, '/html/body/main/div[4]/div/div/div[12]/a').text)
        except:
            pass

        descripcion = card.find_element(By.CSS_SELECTOR, 'div[class="mb-8 break-words"]').text
        try:
            _id = card.find_element(By.CSS_SELECTOR, 'p[class="text-xs font-light"]').text.replace('ID:', '').strip()
        except:
            _id = 'NA'

        url = f"https://www.occ.com.mx/empleo/oferta/{_id}/"
        vacante =  Vacante(
            id=_id,
            titulo=titulo,
            url=url,
            categoria=categoria,
            subcategoria=subcategoria,
            educacion=educacion,
            detalles=detalles,
            descripcion=descripcion
        )
        self.vacancyController.write(vacante.to_dict())
        return vacante

    def set_pages(self):
        self.pages =  int(self.driver.find_element(By.CSS_SELECTOR, 'li.font-light:nth-child(4)').text)

    def next_page(self):
        btn = self.driver.find_elements(By.CSS_SELECTOR, 'ul[class="list-none pl-0 font-sans text-grey-600 text-sm"] > li > svg')[-1]
        btn.click()

    def get_elements_data(self):
        elements = self.get_page_elements()
        elements[0].click()
        self.SLEEP()
        try:
            card = self.driver.find_element(By.CSS_SELECTOR, 'div[class="hidden md:block md:col-span-7 overflow-hidden overflow-y-auto sticky overscroll-contain transition-all duration-300 jobDescription !h-[calc(100vh-232px)] !top-[216px]"]')
        except:
            pass
        for element in elements: 
            try:
                element.click()
                self.SLEEP()
                self.data.append(self.get_vacancy_data(card)) 
            except:
                pass
            

    def quit(self):
        self.driver.close()