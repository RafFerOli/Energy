from pydantic import BaseModel
from typing import Optional, List
from model.Energy import Energy
import json
import numpy as np

# Colunas:

# X1 = Relative Compactness (Compacidade relativa) -  índice utilizado para determinar o grau de compactação de um material granular
# X2 = Surface Area (Área de Superfície)
# X3 = Wall Area (Área da Parede)
# X4 = Roof Area (Área do telhado)
# X5 = Overall Height (Altura total)
# X6 = Orientation (Orientação)
# X7 = Glazing Area (Área de Envidraçamento)
# X8 = Glazing Area Distribution (Distribuição da área envidraçada)

# y1 = Heating Load (Carga de aquecimento)
# y2 = Cooling Load (Carga de resfriamento)

class EnergySchema(BaseModel):
    """ Define como um novo prédio a ser inserido deve ser representado
    """
    name: str = "Predio01"
    comp: float = 0.5
    surf: float = 750.0
    wall: float = 450.0
    roof: float = 250.0
    heig: float = 5.0
    orie: float = 0.15
    gare: float = 25.0
    gdis: float = 30.0

    
class EnergyViewSchema(BaseModel):
    """Define como um prédio será retornado
    """
    id: int = 1
    name: str = "Predio01"
    comp: float = 0.5
    surf: float = 750.0
    wall: float = 450.0
    roof: float = 250.0
    heig: float = 5.0
    orie: float = 0.15
    gare: float = 25.0
    gdis: float = 30.0
    held: float = None
    cold: float = None
    heef: str = None
    coef: str = None
    
class EnergyBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do prédio.
    """
    name: str = "Predio01"

class ListaEnergySchema(BaseModel):
    """Define como uma lista de predios será representada
    """
    predios: List[EnergySchema]

    
class EnergyDelSchema(BaseModel):
    """Define como um prédio para deleção será representado
    """
    name: str = "Predio01"
    
# Apresenta apenas os dados de um paciente    
def apresenta_energy(energy: Energy):
    """ Retorna uma representação do prédio seguindo o schema definido em
        EnergyViewSchema.
    """
    return {
        "id": energy.id,
        "name": energy.name,
        "comp": energy.comp,
        "surf": energy.surf,
        "wall": energy.wall,
        "roof": energy.roof,
        "heig": energy.heig,
        "orie": energy.orie,
        "gare": energy.gare,
        "gdis": energy.gdis,
        "held": energy.held,
        "cold": energy.cold,
        "heef": energy.heef,
        "coef": energy.coef
    }
    
# Apresenta uma lista de predios
def apresenta_energys(energys: List[Energy]):
    """ Retorna uma representação do prédio seguindo o schema definido em
        EnergyViewSchema.
    """
    result = []
    for energy in energys:
        result.append({
                    "id": energy.id,
                    "name": energy.name,
                    "comp": energy.comp,
                    "surf": energy.surf,
                    "wall": energy.wall,
                    "roof": energy.roof,
                    "heig": energy.heig,
                    "orie": energy.orie,
                    "gare": energy.gare,
                    "gdis": energy.gdis,
                    "held": energy.held,
                    "cold": energy.cold,
                    "heef": energy.heef,
                    "coef": energy.coef
        })

    return {"energys": result}

