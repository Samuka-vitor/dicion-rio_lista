atributos = ("Nome", "E-mail", "Profissão")
# lista de dicionários 
usuarios = [
    {
        atributos[0]:"Samuel VItor",
        atributos[1]:"samuelandrade@gmail.com",
        atributos[2]:"namorado",
    },
    {
        atributos[0]: "Cicrano da silva",
        atributos[1]: "lulu@gmail.com",
        atributos[2]: "Administrador",
    },
    {
        atributos[0]:"Beltrano da Saúza",
        atributos[1]:"bet#gmail.com",
        atributos[2]: "contador",
    }
]

# cadastrar novos usuários
usuario = {}
for atributo in atributos:
    usuario[atributo] = input(f"Informe o valor do campo {atributo}.")
usuarios.append(usuario)
    
# exibir os dados na tela de cada usuário
for usuario in usuarios:
        print(" ")
        for atributo in atributos:
            print(f"{atributo}:{usuario.get(atributo)}")