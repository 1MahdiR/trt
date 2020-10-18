
from selenium import webdriver
from bs4 import BeautifulSoup
from shutil import which


def test_webdriver():
    """Testing supported webdrivers."""

    if which('firefox'):
        opt = webdriver.FirefoxOptions()
        opt.headless = True

        return opt, webdriver.Firefox

    elif which('chrome'):
        opt = webdriver.ChromeOptions()
        opt.headless = True

        return opt, webdriver.Chrome

    raise Exception("No supported webdriver is available!")


def translate_text(url):

    opt, driver = test_webdriver()

    der = driver(options=opt)
    der.get(url=url)

    soup = BeautifulSoup(der.page_source, 'html.parser')

    tags = []
    while not tags:
        tags = soup.find_all("span", attrs={'class':'tlid-translation'})

    spans = tags[0].find_all('span')
    text = ""
    for i in spans:
        text += i.get_text() + "\n"

    return text


if __name__ == "__main__":
    print(translate_text("https://translate.google.com/#view=home&op=translate&sl=en&tl=fa&text=hello%20world"))