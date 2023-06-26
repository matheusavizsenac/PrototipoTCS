from flask import jsonify
from model.prompt import Prompts
from model import db
from sqlalchemy import or_

class PromptInstrucaoController:
    def get_instrucoes(self, user_id):
        instrucoes = Prompts.query.filter(or_(Prompts.usuario_id == user_id, Prompts.usuario_id == user_id))
        instrucoes_lista = []
        for instrucoes_gpt in instrucoes:
            instrucoes_lista.append({
                'instrucao': instrucoes_gpt.instrucao,
            })
        return instrucoes_lista

    def get_all_instrucoes(self, user_id):
        instrucoes = Prompts.query.filter(or_(Prompts.usuario_id == user_id, Prompts.usuario_id == user_id))
        return instrucoes

    def insert(self, user_id, instrucao):
        prompt_model = Prompts()
        prompt_model.set_ativo(False)
        prompt_model.set_instrucao(instrucao)
        prompt_model.usuario_id = user_id
        db.session.add(prompt_model)
        db.session.commit()
        return "Success"

    def delete(self, instrucao_id):
        instrucao = Prompts.query.get(instrucao_id)
        db.session.delete(instrucao)
        db.session.commit()
        return "Deleted"