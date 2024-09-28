from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS

# Instanciando o objeto OpenAPI
info = Info(title="Energy API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Importando as rotas
import routes.rts_document
import routes.rts_energy