from selenium import webdriver
from time import time, sleep
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

driver = webdriver.Chrome(executable_path="C:\seleniumbrowserdriverSave\chromedriver.exe")
driver.get("https://www.sahibinden.com/ilan/emlak-konut-satilik-alfa-dan-o-guvenlikli-ve-y-havuzlu-nezih-sitede-super-firsat-1035749580/detay")
Elements = driver.find_element_by_xpath("//*[@id='classifiedDetail']/div/div[2]/div[2]/ul").text
#print(Elements)
DF1 = pd.DataFrame(Elements.split("\n"))
#print(DF) # Bu kısımda verilerimizi data frame halinde bastırıyoruz.
#print(DF1.iloc[3::2].reset_index(drop=True)) # Verileri atlayarak 2'li atlayarak bu şekilde yazdırabi  liriz.
print(DF1)
