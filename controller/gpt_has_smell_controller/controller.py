from flask import session
from sqlalchemy import text
from model.gpt_has_smell import GptHasSmell
from model import db
from model.gpt import Gpt

class GptHasSmellController:

    def __init__(self):
        self.gpt_has_smells = GptHasSmell()

    def get_all_gpt_has_smell(self, user_id):
        query = (
            GptHasSmell.query
            .join(Gpt, Gpt.id == GptHasSmell.id_gpt)
            .filter(Gpt.usuario_id == user_id.id)
        )
        gpt_has_smell = query.all()
        gpt_smell_json = []
        for gpt_smell in gpt_has_smell:
            gpt_smell_json.append({
                'id': gpt_smell.id,
                'id_gpt': gpt_smell.id_gpt,
                'id_smell': gpt_smell.id_smell,
                'descricao_smell': gpt_smell.descricao_smell
            })
        return gpt_smell_json
    
    def get_count_smells(self, smells, user_id):
        id_smell_count = {}
        final_dict = {}
        lista_smells = self.get_all_gpt_has_smell(user_id)
        for i in smells:
            id_smell_count[i["id"]] = 0
        for smell in lista_smells:
            id_smell = smell["id_smell"]
            if id_smell in id_smell_count:
                id_smell_count[id_smell] += 1
            else:
                id_smell_count[id_smell] = 1
        for chave, valor in id_smell_count.items():
            try:
                final_dict[smells[int(chave)-1]['nome']] = valor
            except Exception as e:
                print("Erro" + str(e))
        return final_dict

    def post_smells(self, id_smells, descricao, id_historia):
        for i in id_smells:
            gpt_has_smells = GptHasSmell()
            gpt_has_smells.set_id_gpt(id_historia) 
            gpt_has_smells.set_descricao_smell(descricao)   
            gpt_has_smells.set_id_smell(i)  
            db.session.add(gpt_has_smells)
            db.session.commit()
        return "Success", 200