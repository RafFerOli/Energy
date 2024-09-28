from sklearn.metrics import mean_squared_error, recall_score, precision_score, f1_score
from model.modelo import Model

class Avaliador:

    def avaliar(model, X_test, Y_test):
        """ Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
        avaliação, entre outros.
        """
        predicoes = Model.preditor(model, X_test)
        
        # Caso o seu problema tenha mais do que duas classes, altere o parâmetro average
        return mean_squared_error(Y_test, predicoes)
                
