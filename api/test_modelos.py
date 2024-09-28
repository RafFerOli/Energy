from model import *

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "./MachineLearning/data/ENB2012_data.csv"
colunas = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X1', 'X2']

# Colunas:

# X1 = Relative Compactness (Compacidade relativa) -  índice utilizado para determinar o grau de compactação de um material granular
# X2 = Surface Area (Área de Superfície)
# X3 = Wall Area (Área da Parede)
# X4 = Roof Area (Área do telhado)
# X5 = Overall Height (Altura total)
# X6 = 	Orientation (Orientação)
# X7 = Glazing Area (Área de Envidraçamento)
# X8 = Glazing Area Distribution (Distribuição da área envidraçada)

# y1 = Heating Load (Carga de aquecimento)
# y2 = Cooling Load (Carga de resfriamento)

# Carga dos dados
dataset = Carregador.carregar_dados(url_dados, colunas)

# Separando características (X) e alvos (y1 e y2)
X = dataset.drop(columns=['Y1', 'Y2'])
y1 = dataset['Y1']
y2 = dataset['Y2']
    
# Método para testar o modelo de GradientBoostingRegressor a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"
def test_modelo_gb_Y1():  
    # Importando o modelo de regressão logística
    gb_path_Y1 = './MachineLearning/models/gb_energy_classifier_Y1.pkl'
    modelo_gb_Y1 = Model.carrega_modelo(gb_path_Y1)

    # Obtendo as métricas da Regressão Logística
    error_gb_Y1 = Avaliador.avaliar(modelo_gb_Y1, X, y1)
    
    # Testando as métricas do gb
    # Modifique as métricas de acordo com seus requisitos
    assert error_gb_Y1 >= 5

# Método para testar o modelo de GradientBoostingRegressor a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"
def test_modelo_gb_Y2():  
    # Importando o modelo de regressão logística
    gb_path_Y2 = './MachineLearning/models/gb_energy_classifier_Y2.pkl'
    modelo_gb_Y2 = Model.carrega_modelo(gb_path_Y2)

    # Obtendo as métricas da Regressão Logística
    error_gb_Y2 = Avaliador.avaliar(modelo_gb_Y2, X, y2)
    
    # Testando as métricas do gb
    # Modifique as métricas de acordo com seus requisitos
    assert error_gb_Y2 >= 5


    

