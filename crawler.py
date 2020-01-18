from selenium import webdriver
import time


class Globo:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://www.globo.com/' # url a ser crawleada
        self.wrapper = 'hui-premium'
        # self.wrapper = 'hui-premium__title'
        self.list = []

    # Inicia a navegação
    def navigate(self):
        self.driver.get(self.url)

    def get_noticias(self):
        noticias = self.driver.find_elements_by_class_name(self.wrapper)
        import ipdb; ipdb.set_trace()
        for noticia in noticias:
            images = noticia.find_elements_by_tag_name('img')
            sub = noticia.find_elements_by_class_name('hui-premium__related')
            for image in images:
                dict = {
                    'title': noticia.text,
                    'sub_title': [subtitle.text for subtitle in sub],
                    'url_img': image.get_attribute('src') if image.get_attribute('src') else '-'
                }
                self.list.append(dict)
        print(self.list)
        self.driver.close()

# Web driver Firefox
wbf = webdriver.Firefox()

# Instanciando o objeto
globo = Globo(wbf)

# Navegando
globo.navigate()

time.sleep(5)
globo.get_noticias()