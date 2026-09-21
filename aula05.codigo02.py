nt("\n-------------------")
print("  CABEÇALHO GERAL  ")
print("-------------------")

#criando um dicionario
aluno={
"nome":"Alexandro Heitor","disciplina": "Python básico", "nota": "Valparaíso de Goiás"
    }
#usando as F-Strings e acessando as chaves do dicionario
print(f"⛲ Aluno(a):{aluno['nome']}")
print(f"⛲ disciplina:{aluno['disciplina']}")
print(f"⛲ nota:{aluno['nota']}")

from datetime import datetime
data_formada=datetime.now().strftime("%d/%m/%y")

#usando f-string para ajustar o texto com a variavel
print(f"⛩️ Data{data_formada}")

#saída: data 21/09/2026
print("----------------------")
