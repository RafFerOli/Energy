# Importando instâncias para rodar flask
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

# Importando instâncias para rodar sqlalchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func

# Importando instancias gerais
from logger import logger
from schemas import *
from model import *

# Importando a instância do app criada em app.py
from app import app

# Definindo tags para agrupamento das rotas
energy_tag = Tag(name="Predio", description="Adição, visualização, remoção e predição de prédios para avaliação")

#-------------------------------------------------------------------------------------
# Post: Energy
#-------------------------------------------------------------------------------------
@app.post('/energy', tags=[energy_tag],
          responses={"200": EnergyViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: EnergySchema):
    """Adiciona um novo prédio à base de dados
    Retorna uma representação dos prédios e predições associadas.
    
    Args:

        name (str): nome do prédio
        comp (float): Relative Compactness (Compacidade relativa)
        surf (float): Surface Area (Área de Superfície)
        wall (float): Wall Area (Área da Parede)
        roof (float): Roof Area (Área do telhado)
        heig (float): Overall Height (Altura total)
        orie (float): Orientation (Orientação)
        gare (float): Glazing Area (Área de Envidraçamento)
        gdis (float): Glazing Area Distribution (Distribuição da área envidraçada)        
               
    Returns:

        held (float): Heating Load (Carga de aquecimento)
        cold (float): Cooling Load (Carga de resfriamento)                
        heef (str): Heating Efficiency (Eficiência  de aquecimento)
        coef (str): Cooling Efficiency (Eficiência  de resfriamento)   
    """

    # Recuperando os dados do formulário
    name = form.name
    comp = form.comp
    surf = form.surf
    wall = form.wall
    roof = form.roof
    heig = form.heig
    orie = form.orie
    gare = form.gare
    gdis = form.gdis
        
    # Preparando os dados para o modelo
    X_input = PreProcessador.preparar_form(form)

    # Carregando modelo
    model_path_Y1 = './MachineLearning/pipelines/gb_energy_pipeline_Y1.pkl'    
    model_path_Y2 = './MachineLearning/pipelines/gb_energy_pipeline_Y2.pkl'    

    # modelo = Model.carrega_modelo(ml_path)
    modelo_Y1 = Pipeline.carrega_pipeline(model_path_Y1)
    modelo_Y2 = Pipeline.carrega_pipeline(model_path_Y2)
    
    # Realizando a predição    
    held = float(format(Model.preditor(modelo_Y1, X_input)[0], '.2f'))
    cold = float(format(Model.preditor(modelo_Y2, X_input)[0], '.2f'))
       
    # Classificação das predições em categorias
    heef = categorize(held)
    coef = categorize(cold)       

    energy = Energy(
        name = name,
        comp = comp,
        surf = surf,
        wall = wall,
        roof = roof,
        heig = heig,
        orie = orie,
        gare = gare,
        gdis = gdis,
        held = held,
        cold = cold,
        heef = heef,
        coef = coef
    )
    logger.debug(f"Adicionando produto de nome: '{energy.name}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se prédio já existe na base
        if session.query(Energy).filter(Energy.name == form.name).first():
            error_msg = "Prédio já existente na base :/"
            logger.warning(f"Erro ao adicionar prédio '{energy.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando prédio
        session.add(energy)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado prédio de nome: '{energy.name}'")
        return apresenta_energy(energy), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar prédio '{energy.name}', {error_msg}")
        return {"message": error_msg}, 400

#-------------------------------------------------------------------------------------
# Delete: Energy
#-------------------------------------------------------------------------------------

@app.delete('/energy', tags=[energy_tag],
            responses={"200": EnergyViewSchema, "404": ErrorSchema})
def delete_energy(query: EnergyBuscaSchema):
    """Remove um prédio cadastrado na base a partir do nome

    Args:
        nome (str): nome do prédio
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    energy_nome = unquote(query.name)
    logger.debug(f"Deletando dados sobre prédio #{energy_nome}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando prédio
    energy = session.query(Energy).filter(Energy.name == energy_nome).first()
    
    if not energy:
        error_msg = "Prédio não encontrado na base :/"
        logger.warning(f"Erro ao deletar prédio '{energy_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(energy)
        session.commit()
        logger.debug(f"Deletado prédio #{energy_nome}")
        return {"message": f"Prédio {energy_nome} removido com sucesso!"}, 200

#-------------------------------------------------------------------------------------
# Put: Energy
#-------------------------------------------------------------------------------------

@app.put('/energy', tags=[energy_tag],
          responses={"200": EnergyViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def put_Energy(form: EnergySchema):
    """Modifica um prédio da base de dados

    Retorna uma mensagem de confirmação da modificação.
    """
    energy_nome = unquote(unquote(form.name))
    print(energy_nome)
    logger.debug(f"Modificando dados sobre o prédio #{energy_nome}")
    # criando conexão com a base
    session = Session()

    # selecinando linha que se deseja alterar
    count = session.query(Energy).filter(func.lower(Energy.name) == energy_nome.lower()).first()

    # Atualizando valores do registro
    count.name = form.name
    count.comp = form.comp
    count.surf = form.surf
    count.wall = form.wall
    count.roof = form.roof
    count.heig = form.heig
    count.orie = form.orie
    count.gare = form.gare
    count.gdis = form.gdis

    # Preparando os dados para o modelo
    X_input = PreProcessador.preparar_form(form)

    # Carregando modelo
    model_path_Y1 = './MachineLearning/pipelines/gb_energy_pipeline_Y1.pkl'    
    model_path_Y2 = './MachineLearning/pipelines/gb_energy_pipeline_Y2.pkl'  

    # modelo = Model.carrega_modelo(ml_path)
    modelo_Y1 = Pipeline.carrega_pipeline(model_path_Y1)
    modelo_Y2 = Pipeline.carrega_pipeline(model_path_Y2)
    
    # Realizando a predição    
    count.held = float(format(Model.preditor(modelo_Y1, X_input)[0], '.2f'))
    count.cold = float(format(Model.preditor(modelo_Y2, X_input)[0], '.2f'))

    # Classificação das predições em categorias
    count.heef = categorize(count.held)
    count.coef = categorize(count.cold)

    # Confirme as alterações no banco de dados 
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Modificado Prédio #{energy_nome}")
        return {"mesage": "Prédio modificado", "Nome": energy_nome}
    else:
        # se o Prédio não foi encontrado
        error_msg = "Prédio não encontrado na base :/"
        logger.warning(f"Erro ao Modificar Prédio #'{energy_nome}', {error_msg}")
        return {"mesage": error_msg}, 404

#-------------------------------------------------------------------------------------
# Get: Energys
#-------------------------------------------------------------------------------------

@app.get('/energys', tags=[energy_tag],
         responses={"200": EnergyViewSchema, "404": ErrorSchema})
def get_energys():
    """Lista todos os prédios cadastrados na base
    Args:
       none
        
    Returns:
        list: lista de prédios cadastrados na base
    """
    logger.debug("Coletando dados sobre todos os prédios")
    # Criando conexão com a base
    session = Session()
    # Buscando todos os prédios
    energys = session.query(Energy).all()
    
    if not energys:
        # Se não houver prédios
        return {"prédios": []}, 200
    else:
        logger.debug(f"%d prédios econtrados" % len(energys))
        print(energys)
        return apresenta_energys(energys), 200

#-------------------------------------------------------------------------------------
# Get: Energy (query: nome)
#-------------------------------------------------------------------------------------

@app.get('/energy', tags=[energy_tag],
         responses={"200": EnergyViewSchema, "404": ErrorSchema})
def get_energy(query: EnergyBuscaSchema):    
    """Faz a busca por um prédio cadastrado na base a partir do nome

    Args:
        nome (str): nome do prédio
        
    Returns:
        dict: representação do prédio e predição associada
    """
    
    energy_nome = query.name
    logger.debug(f"Coletando dados sobre prédio #{energy_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    energy = session.query(Energy).filter(Energy.name == energy_nome).first()
    
    if not energy:
        # se o prédio não foi encontrado
        error_msg = f"Prédio {energy_nome} não encontrado na base :/"
        logger.warning(f"Erro ao buscar prédio '{energy_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Prédio encontrado: '{energy.name}'")
        # retorna a representação do prédio
        return apresenta_energy(energy), 200
    
#-------------------------------------------------------------------------------------
# Auxilizares
#-------------------------------------------------------------------------------------

    # Classificação das predições em categorias
def categorize(value):
    if value >= 30:
        return 'Alta'
    elif value >= 15:
        return 'Média'
    else:
        return 'Baixa'