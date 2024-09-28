from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# Colunas:

# X1 = Relative Compactness (Compacidade relativa) -  índice utilizado para determinar o grau de compactação de um material granular
# X2 = Surface Area (Área de Superfície)
# X3 = Wall Area (Área da Parede)
# X4 = Roof Area (Área do Telhado)
# X5 = Overall Height (Altura Total)
# X6 = 	Orientation (Orientação)
# X7 = Glazing Area (Área de Envidraçamento)
# X8 = Glazing Area Distribution (Distribuição da área envidraçada)

# y1 = Heating Load (Carga de aquecimento)
# y2 = Cooling Load (Carga de resfriamento)


class Energy(Base):
    __tablename__ = 'energy'
    
    id = Column(Integer, primary_key=True)
    name= Column("name", String(50), unique=True) 
    #colunas de entrada
    comp = Column("comp", Float)
    surf = Column("surf", Float)
    wall = Column("wall", Float)
    roof = Column("roof", Float)
    heig = Column("heig", Float)
    orie = Column("orie", Float)
    gare = Column("gare", Float)
    gdis = Column("gdis", Float)
    #colunas de saída 
    held = Column("held", Float)
    cold = Column("cold", Float)
    heef = Column("heef", String)
    coef = Column("coef", String)    

    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, name:str, comp:float, 
                 surf:float, wall:float, roof:float,
                 heig:float, orie:float, gare:float, 
                 gdis:float, held:float, cold:float, 
                 heef:str, coef:str, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um prédio

        Arguments:
        name: nome do prédio
        comp: Relative Compactness (Compacidade relativa)
        surf: Surface Area (Área de Superfície)
        wall: Wall Area (Área da Parede)
        roof: Roof Area (Área do telhado)
        heig: Overall Height (Altura total)
        orie: Orientation (Orientação)
        gare: Glazing Area (Área de Envidraçamento)
        gdis: Glazing Area Distribution (Distribuição da área envidraçada)
        held: Heating Load (Carga de aquecimento)
        cold: Cooling Load (Carga de resfriamento)
        heef: Heating efficiency (Eficiência  de aquecimento)
        coef: Cooling efficiency (Eficiência  de resfriamento)
        data_insercao: data de quando o paciente foi inserido à base
        """

        self.name = name
        self.comp = comp
        self.surf = surf
        self.wall = wall
        self.roof = roof
        self.heig = heig
        self.orie = orie
        self.gare = gare
        self.gdis = gdis
        self.held = held
        self.cold = cold
        self.heef = heef
        self.coef = coef
  
        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao