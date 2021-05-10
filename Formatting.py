def format(privateKey, publicKey, assinatura):
  f = open("result.pem", "w+")

  f.write("-----BEGIN PRIVATE KEY-----\n")
  f.write(str(privateKey))
  f.write("\n-----END PRIVATE KEY-----\n")

  
  f.write("-----BEGIN PUBLIC KEY-----\n")
  f.write(str(publicKey))
  f.write("\n-----END PUBLIC KEY-----\n")

  f.write("-----BEGIN CERTIFICATE-----\n")
  f.write(str(assinatura))
  f.write("\n-----END CERTIFICATE-----\n")


  f.close()
