from enviaram_tarefa import confere_envio, nao_enviaram

turma1 = {
    "Pedro": True,
    "Lucas" : False,
    "Murilo" : True,
    "Ana" : False,
    "Julia" : True,
    "Fernando" : False,
    "Vitor" : True,
    "Jheimisson" : False,
    "Vinicius" : True,
    "Renato" : False
}

turma2 = {
    "Pedro": False,
    "Lucas" : True,
    "Murilo" : False,
    "Ana" : True,
    "Julia" : False,
    "Fernando" : True,
    "Vitor" : False,
    "Jheimisson" : True,
    "Vinicius" : False,
    "Renato" : True
}

def testconfireEnvio():
  print ('Cofere envio')
  assert confere_envio(turma1) == ["Pedro", "Murilo", "Julia", "Vitor", "Vinicius"]
  assert confere_envio(turma2) == ["Lucas", "Ana", "Fernando", "Jheimisson", "Renato"]


def testnaoEnviaram():
  print ('Não enviaram')
  assert nao_enviaram(turma1) == ["Lucas", "Ana", "Fernando", "Jheimisson", "Renato"]
  assert nao_enviaram(turma2) == ["Pedro", "Murilo", "Julia", "Vitor", "Vinicius"]