const defaultCode = `print("Hello world whit python")

palabra= list("casa")
n=len(palabra)
letra=""
vidas=6
entrada = [" - " for _ in range(n)] #Listas de comprension
encontrado=False

print("Bienvenido al juego del ahorcado")
print(f"Cuentas con: {vidas} vidas")
print(f"Estado actual: {entrada}")


while(entrada != palabra):
    letra=input("Ingresa una letra")
    for i in range(n):
        if palabra[i]==letra:
            print(f"Si existe: {letra} en la pocision {i}")
            entrada[i]=letra
            encontrado=True

    if not encontrado:
        print(f"La letra {letra} no existe")
        vidas-=1

    print(f"Estado actual: {entrada}")
    print(f"Vidas restantes: {vidas}")    

    if vidas==0:
        print("Perdiste :(")
        break

    encontrado=False
    print()
    
    if entrada==palabra:
        print("Felicidades ganaste")
`;


window.onload = () => {
    const codeEditor = document.getElementById('codeEditor');
    codeEditor.value = defaultCode; 
};




