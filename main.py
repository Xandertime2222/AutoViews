from selenium import webdriver
import time
views = input("Wie viele Views möchten sie?")
viewsint = int(views)
driver = webdriver.Chrome('C:\\Users\Alexander\\Desktop\\JAVA\\chromedriver.exe')
driver.get('https://www.youtube.com/watch?v=VH_dvwy216U')
print ("Es dauert ",viewsint * 3, "Sekunden")
for i in range(viewsint):
    driver.refresh()
    time.sleep(3)
driver.close()


