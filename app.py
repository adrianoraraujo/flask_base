# -*- coding: UTF-8 -*-
from flask import Flask, request, render_template, url_for, redirect # Importa a biblioteca
from flask import Flask, send_file
from flask_sqlalchemy import SQLAlchemy
import requests
import json
import xlwt
import xlrd
import time, sys
import re
import os


app = Flask(__name__) # Inicializa a aplicação
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:senha@endereco/nome_db'

db = SQLAlchemy(app)

class Tabela_1(db.Model):
   __tablename__='tabela_1'
   _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   nome = db.Column(db.String(50))
   email = db.Column(db.String(50))
   tel= db.Column(db.String(11))
   cel= db.Column(db.String(11))
   senha= db.Column(db.String(20))




   def __init__(self, nome,email, tel, cel, senha):
      self.nome= nome
      self.email=email
      self.tel=tel
      self.cel=cel
      self.senha
     

class Tabela_2(db.Model):
   __tablename__='tabela_2'
   _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   mes = db.Column(db.Integer)
   ano = db.Column(db.Integer)
   valor = db.Column(db.Float)
   tabela_1_id= db.Column(db.Integer, db.ForeignKey('tabela_1._id'))
   tabela_1 = db.relationship('Tabela_1')
   
   def __init__(self, mes, ano, valor, tabela_1_id):
      self.mes=mes
      self.ano=ano
      self.valor=valor
      self.tabela_1_id=tabela_1_id




   

db.create_all()


'''
nomeUser=''

@app.route('/') # Nova rota
def main():
    
   return render_template('home.html')   

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=sys.argv[1]) # Executa a aplicação
   #app.run(debug=True)
