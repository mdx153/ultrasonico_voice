#pip install pyserial
#pip install pyttsx3

import serial
import pyttsx3

serialArd = serial.Serial('COM3', 9600)
assistente = pyttsx3.init()

while True:
    #[2:-5] remove \n,\b que vem junto na leitura
    textoConvertido = str(serialArd.readline())[2:-5]
    print(textoConvertido)
    assistente.say("Objeto encontrado a " + textoConvertido + " centimetro")
    assistente.runAndWait()

#serialArd.write(dado.encode()) //envia dados p/ arduino
#serial.flush() //limpa a comunicação