import tkinter as tk
import pyttsx3
import speech_recognition as sr

class CasaInteligente:
    def __init__(self):
        self.luzes = False
        self.tomadas = False

    def ligar_luzes(self):
        self.luzes = True
        return "As luzes foram ligadas!"

    def desligar_luzes(self):
        self.luzes = False
        return "As luzes foram desligadas!"

    def ligar_tomadas(self):
        self.tomadas = True
        return "As tomadas inteligentes foram ligadas!"

    def desligar_tomadas(self):
        self.tomadas = False
        return "As tomadas inteligentes foram desligadas!"

    def rotina_boa_noite(self):
        self.desligar_luzes()
        self.desligar_tomadas()
        return 'Rotina "Boa noite" acionada.'

    def rotina_chegada(self):
        self.ligar_luzes()
        self.ligar_tomadas()
        return 'Rotina de chegada acionada.'

    def status(self):
        return f"Luzes: {'Ligadas' if self.luzes else 'Desligadas'}
Tomadas inteligentes: {'Ligadas' if self.tomadas else 'Desligadas'}"

class App:
    def __init__(self, root):
        self.casa = CasaInteligente()
        self.root = root
        self.root.title('Automação Residencial com Alexa - Simulador')
        self.engine = pyttsx3.init()
        self.build_ui()

    def build_ui(self):
        tk.Button(self.root, text='Ligar todas as luzes', command=self.ligar_luzes).pack(fill='x')
        tk.Button(self.root, text='Desligar todas as luzes', command=self.desligar_luzes).pack(fill='x')
        tk.Button(self.root, text='Rotina "Boa noite"', command=self.rotina_boa_noite).pack(fill='x')
        tk.Button(self.root, text='Rotina de chegada', command=self.rotina_chegada).pack(fill='x')
        tk.Button(self.root, text='Mostrar status', command=self.status).pack(fill='x')
        tk.Button(self.root, text='Comando de voz', command=self.ouvir_comando).pack(fill='x')
        self.status_label = tk.Label(self.root, text='Status:')
        self.status_label.pack(pady=8)

    def falar(self, texto):
        self.engine.say(texto)
        self.engine.runAndWait()

    def ligar_luzes(self):
        msg = self.casa.ligar_luzes()
        self.status_label['text'] = msg
        self.falar(msg)

    def desligar_luzes(self):
        msg = self.casa.desligar_luzes()
        self.status_label['text'] = msg
        self.falar(msg)

    def rotina_boa_noite(self):
        msg = self.casa.rotina_boa_noite()
        self.status_label['text'] = msg
        self.falar(msg)

    def rotina_chegada(self):
        msg = self.casa.rotina_chegada()
        self.status_label['text'] = msg
        self.falar(msg)

    def status(self):
        msg = self.casa.status()
        self.status_label['text'] = msg
        self.falar(msg)

    def ouvir_comando(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.status_label['text'] = 'Ouvindo comando...'
            self.falar('Estou ouvindo seu comando.')
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        try:
            comando = recognizer.recognize_google(audio, language='pt-BR').lower()
            if 'ligar luz' in comando:
                self.ligar_luzes()
            elif 'desligar luz' in comando:
                self.desligar_luzes()
            elif 'boa noite' in comando:
                self.rotina_boa_noite()
            elif 'chegada' in comando:
                self.rotina_chegada()
            elif 'status' in comando:
                self.status()
            else:
                msg = 'Comando não reconhecido.'
                self.status_label['text'] = msg
                self.falar(msg)
        except Exception as e:
            msg = f'Erro ao reconhecer comando: {e}'
            self.status_label['text'] = msg
            self.falar(msg)

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
