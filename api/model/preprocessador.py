from sklearn.model_selection import train_test_split
import pickle
import numpy as np

class PreProcessador:

    def separa_teste_treino(self, dataset, percentual_teste, seed=7):
        """ Cuida de todo o pré-processamento. """
        # limpeza dos dados e eliminação de outliers

        # feature selection

        # Codificando as variáveis categóricas em uma cópia do dataset
        dataset_encoded = dataset.copy()  # Faz uma cópia do dataset original
        label_encoders = {}

        # Codificando as variáveis categóricas
        for column in dataset_encoded.select_dtypes(include=['object']).columns:
            le = LabelEncoder()
            dataset_encoded[column] = le.fit_transform(dataset_encoded[column])
            label_encoders[column] = le

        # divisão em treino e teste Y1
        X_train, X_test, Y1_train, Y1_test = self.__preparar_Y1(dataset,
                                                                  percentual_teste,
                                                                  seed)
        
        # divisão em treino e teste Y2
        X_train, X_test, Y2_train, Y2_test = self.__preparar_Y2(dataset,
                                                                  percentual_teste,
                                                                  seed)
        
        # normalização/padronização        
        return (X_train, X_test, Y1_train, Y1_test, Y2_train, Y2_test)
    
    def __preparar_Y1(self, dataset, percentual_teste, seed):
        """ Divide os dados em treino e teste usando o método __preparar_Y1.
        Assume que a variável target está na última coluna.
        O parâmetro test_size é o percentual de dados de teste.
        """
        # Separando características (X) e alvos (y1 e y2)
        X = dataset.drop(columns=['Y1', 'Y2'])
        y1 = dataset['Y1']        

        return train_test_split(X, y1, test_size=percentual_teste, random_state=seed)
    
    def __preparar_Y2(self, dataset, percentual_teste, seed):
        """ Divide os dados em treino e teste usando o método __preparar_Y2.
        Assume que a variável target está na última coluna.
        O parâmetro test_size é o percentual de dados de teste.
        """
        # Separando características (X) e alvos (y1 e y2)
        X = dataset.drop(columns=['Y1', 'Y2'])
        y2 = dataset['Y2']        

        return train_test_split(X, y2, test_size=percentual_teste, random_state=seed)


    def preparar_form(form):
        """ Prepara os dados recebidos do front para serem usados no modelo. """
        X_input = np.array([form.comp, 
                            form.surf, 
                            form.wall, 
                            form.roof, 
                            form.heig, 
                            form.orie, 
                            form.gare, 
                            form.gdis
                        ])
        # Faremos o reshape para que o modelo entenda que estamos passando
        X_input = X_input.reshape(1, -1)
        return X_input
    
    def scaler(X_train):
        """ Normaliza os dados. """
        # normalização/padronização
        scaler = pickle.load(open('./MachineLearning/scalers/minmax_scaler_energy.pkl', 'rb'))
        reescaled_X_train = scaler.transform(X_train)
        return reescaled_X_train
