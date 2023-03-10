import rsa

(pubchave, chavepriv) = rsa.newkeys(512)

texto = input("Texto para criptografia: \n")

criptotexto = rsa.encrypt(texto.encode(), pubchave)
acripto = rsa.decrypt(criptotexto, chavepriv).decode()

print(f'Texto original: {texto} e seu tamanho: {len(texto)}')
print(f'Chave pub: {pubchave}')
print(f'Chave priv: {chavepriv}')
print(f'Texto criptografado: {criptotexto}')
