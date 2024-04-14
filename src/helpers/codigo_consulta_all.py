from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Criar um engine de conexão com o banco de dados local passando usuario e senha
engine = create_engine('postgresql://postgres:32133@localhost:5432/postgres')

# Criar uma instância da base usando a declarative_base
Base = declarative_base()

# aqui eu crio uma calsse para representar minha tabela cadastro no banco de dados localhots
class User(Base):
    __tablename__ = 'cadastro'

    id = Column(Integer, primary_key=True)
    nome = Column(String(55))
    cpf = Column(String(11))
    rua = Column(String(55))
    telefone = Column(String(55))

# Crio uma sessão (conexao) para poder interagir com o banco
Session = sessionmaker(bind=engine)
session = Session()

# Realizo uma consulta (SELECT *) na tabela cadastro 
users = session.query(User).all()

# print nos resultados de acordo com cada coluna
for user in users:
    print(user.nome, user.cpf, user.rua, user.telefone)

# Fechar a sessão (para nao ficar aberta no banco)
session.close()
