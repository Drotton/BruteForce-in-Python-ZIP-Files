#pip3 install tqdm

import zipfile
from tqdm import tqdm

#Lista de senhas - Tem que estar no mesmo diretorio - .txt
wordlist = ""
#Arquivo alvo
zip_file = ""
#inicializando o objeto
zip_file = zipfile.ZipFile(zip_file)
#Contando o numero de senhas na lista
n_words = len(list(open(wordlist, "rb")))
#Printa o numero de senhas
print("Nº de senhas:", n_words)

#Teste de senhas
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Senha não encontrada.")