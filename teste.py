from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
from time import sleep

# iniciar o chrome em segundo plano
chrome_options = Options()
chrome_options.headless = True
driver = webdriver.Chrome(options=chrome_options)

# acessar o site e aguardar 10 segundos para pegar a velocidade
driver.get('https://fast.com/pt/')
sleep(6)
velocidade = driver.find_element('xpath', '//*[@id="speed-value"]').text

# encerrar o chrome
driver.quit()

# pegar data e hora atual
data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# criar dataframe com data e velocidade
df = pd.read_excel('teste-velocidade.xlsx')
df_novo = pd.DataFrame(columns=['Data', 'Velocidade'])
df_novo['Data'] = [data]
df_novo['Velocidade'] = [velocidade]

# salvar o dataframe em um arquivo excel atualizado
df = df.append(df_novo, ignore_index=True)
df.to_excel('teste-velocidade.xlsx', index=False)
