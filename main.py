import openai
from dotenv import load_dotenv
import subprocess
import os

load_dotenv()

openai.api_key = os.getenv("OPEN_API_KEY")


def gerarComandoShell(texto):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Escreva um comando cmdlet que faça o seguinte: {texto}",
        temperature=0.7,
        max_tokens=2048,
        n=1,
        stop=None
    )
    return response['choices'][0]['text'].strip()


def executarComandoShell(comando):
    try:
        resultado = subprocess.run(comando, shell=True, check=True)
        print(resultado)
    except subprocess.CalledProcessError as e:
        print(e)


descricao_comando = input("Digite a descrição para o comando shell: ")
comando = gerarComandoShell(descricao_comando)
print(f"Comando gerado:{comando}")
executarComandoShell(comando)
