import pandas as pd
from Regex import Regex
from Extraction import Extraction
from utils.Charts import Charts


regexObject = Regex()
extractionObject = Extraction()
chartsObject = Charts()

news = {i: f"news/{i}.txt" for i in range(1, 21)} # declara um array indexado para armazenar o caminho das noticias na pasta news

df = pd.read_csv('datasets/MOCK_DATA.csv')

# print(df.to_json())

timestamp = df['timestamp']
user_name = df['name'] 
user_age = df['age']
user_state = df['state'] 
df['gender'] = df['gender'].apply(lambda x: 'M' if x == 'Male' else 'F') # caso o valor do gender for igual a "Male" ele aplica o valor M, caso não ele aplica F
news_id = df['news_id']
time_spent = df['time_spent']
device = df['device']

df['category'] = news_id.apply(lambda x: regexObject.identifyNewsCategory(news[int(x)])) # para cada iteração do news_id ele pega o 
                                                                                            #   valor e aplica o identify para verificar qual é a categoria 
                                                                                            #   que mais se identifica baseado em REGEX

category_counts = df['category'].value_counts() ## faz a contagem das categorias, para gerar o gráfico

chartsObject.generatePieChart(category_counts)
# extract_dataset_by_state(df)

