from back.config.config import db
# clearfrom back.model.import_model import *
import os

# criar tabelas
db.create_all()

print("Banco de dados e tabelas criadas")