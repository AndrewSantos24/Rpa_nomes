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

def save_daddos_banco(nomes,cpfs,endereco,telefones):
    
    # Crio uma sessão (conexao) para poder interagir com o banco
    Session = sessionmaker(bind=engine)
    session = Session()

    # aqui vou inserindo em cadda coluna os dados que preciso
    novo_usuario = User(nome=str(nomes), cpf=str(cpfs), rua=str(endereco), telefone=str(telefones))

    # fazendo insert no banco de dados local
    session.add(novo_usuario)

    # commitando as alteraçoes
    session.commit()

    # Fecho a sessao
    session.close()