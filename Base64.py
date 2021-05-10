import sys

def encodeBase64(s):

  i = 0
  base64 = ending = ''
  base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
  
  # Adiciona padding se a string não for divisível por 3
  pad = 3 - (len(s) % 3)
  if pad != 3:
    s += "A" * pad
    ending += '=' * pad
  
  # Itera através da string
  while i < len(s):
    b = 0

    #  De 3 em 3 caracteres, os converte para 4 chars base64
    for j in range(0,3,1):
      
      #  Pega o código ASCII do próximo caractere na linha
      n = ord(s[i])
      i += 1
  
      # Concatena os três caracteres juntos
      b += n << 8 * (2-j)
    
    # Converte os 3 chars para 4 chars base64
    base64 += base64chars[ (b >> 18) & 63 ]
    base64 += base64chars[ (b >> 12) & 63 ]
    base64 += base64chars[ (b >> 6) & 63 ]
    base64 += base64chars[ b & 63 ]

  # Adiciona o padding no final
  if pad != 3:
    base64 = base64[:-pad]
    base64 += ending

  return base64


def decodeBase64(s):
  i = 0
  base64 = decoded = ''
  base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
  
  # Substitui o padding com caracteres "A" para o decoder processar a string e salvar o tamanho do padding
  if s[-2:] == '==':
    s = s[0:-2] + "AA"
    padd = 2
  elif s[-1:] == '=':
    s = s[0:-1] + "A"
    padd = 1
  else:
    padd = 0

  #  Digere 4 caracteres por vez
  while i < len(s):
    d = 0
    for j in range(0,4,1):
      
      d += base64chars.index( s[i] ) << (18 - j * 6)
      i += 1

    # Converte os 4 chars de volta ao ASCII
    decoded += chr( (d >> 16 ) & 255 )
    decoded += chr( (d >> 8 ) & 255 )
    decoded += chr( d & 255 )
  
  # Remove padding
  decoded = decoded[0:len( decoded ) - padd]

  return decoded

if __name__ == "__main__":
  # s = "its britney bitch"

  # encodeBase64(s)

  d = "aXRzIGJyaXRuZXkgYml0Y2h="

  r = decodeBase64(d)

  print(r)

