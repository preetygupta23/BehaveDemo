from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context,driver):
    context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


def after_step(context,step):
    print()
