import requests  # Add requests for GitHub API calls
import os
from random import shuffle
import time
import re
import sys
import wikipediaapi
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QTextBrowser, QSpacerItem, QSizePolicy

conversazione = []

# Add your GitHub token here (store securely in a real application)
GITHUB_TOKEN = 'your_github_token'

class ChatApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Krysto's (not so) Revolutionary Bot Beta-1")
        self.setGeometry(100, 100, 600, 500)

        # Dark mode colors
        self.setStyleSheet("background-color: #1E1E1E;")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        # Chat box with teal background
        self.chat_box = QTextBrowser(self)
        self.chat_box.setStyleSheet("""
            font-size: 18px;
            background-color: #252526;
            color: #D4D4D4;
            border: 2px solid #00796B;
            border-radius: 10px;
        """)
        layout.addWidget(self.chat_box)

        # Input field with rounded corners
        self.input_field = QLineEdit(self)
        self.input_field.setStyleSheet("""
            font-size: 18px;
            background-color: #333333;
            color: #E0E0E0;
            border: 2px solid #00796B;
            padding: 8px;
            border-radius: 10px;
        """)
        layout.addWidget(self.input_field)

        self.input_field.returnPressed.connect(self.rispondi)

        button_layout = QHBoxLayout()

        # Send button with teal color and rounded corners
        send_button = QPushButton("Send", self)
        send_button.setStyleSheet("""
            font-size: 18px;
            background-color: #00796B;
            color: white;
            border-radius: 10px;
            padding: 10px;
        """)
        send_button.setFixedHeight(40)
        button_layout.addWidget(send_button)
        send_button.clicked.connect(self.rispondi)

        # Spacer between buttons
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        button_layout.addItem(spacer)

        # Clear button with red color and rounded corners
        clear_button = QPushButton("Clear", self)
        clear_button.setStyleSheet("""
            font-size: 18px;
            background-color: #D32F2F;
            color: white;
            border-radius: 10px;
            padding: 10px;
        """)
        clear_button.setFixedHeight(40)
        button_layout.addWidget(clear_button)
        clear_button.clicked.connect(self.clear_chat)

        layout.addLayout(button_layout)

        self.central_widget.setLayout(layout)

    def rispondi(self):
        input_utente = self.input_field.text().strip()
        if input_utente:
            messaggio_utente = "TU: " + input_utente
            conversazione.append(messaggio_utente)
            self.chat_box.append(messaggio_utente)

            global emo #lol funny hahaha
            if not messaggio_utente.startswith('TU: /wikipedia '):
                if "hello" in messaggio_utente.lower() or "hi" in messaggio_utente.lower():
                    risposta_bot = "Hi!\nI'm Krysto's Bot, how can i help you?"
                elif "how are you" in messaggio_utente.lower() or "how's it going" in messaggio_utente.lower():
                    risposta_bot = "Good, you?"
                elif "im fine" in messaggio_utente.lower():
                    risposta_bot = "thats good"
                elif "not very good" in messaggio_utente.lower() or "bad" in messaggio_utente.lower():
                    risposta_bot = "r u emo?"
                elif "i'm not emo" in messaggio_utente.lower():
                        risposta_bot = "yeah yeah of course no"
                elif "global emo" in messaggio_utente.lower():

                    # Ottieni il percorso assoluto della directory corrente
                    directory_corrente = os.getcwd()


                    # Crea un'espressione regolare per trovare il nome dell'utente dopo "user/"
                    pattern = re.compile(r'Users[\\/]([^\\/]+)')

                    # Cerca il nome dell'utente nella directory corrente
                    match = pattern.search(directory_corrente)

                    # Estrai il nome dell'utente se trovato
                    if match:
                        nome_utente = match.group(1)

                    risposta_bot = f"YK WHAT? YOURE A BIG MORON /ban {nome_utente}"
                    directory_corrente = os.getcwd()
                elif "What does k.r.b mean?" in messaggio_utente.lower() or "k.r.b" in messaggio_utente.lower() or "krb" in messaggio_utente.lower():
                    risposta_bot = "youre so silly, it means Krysto Revolutionary Bot"
                elif "i can still feel him" in messaggio_utente.lower():
                    risposta_bot = "-. -. ..--- -.. -- -.. -..- -.. --- --.. ....-"
                elif "youre chilling" in messaggio_utente.lower() or "youre chill" in messaggio_utente.lower():
                    risposta_bot = "yeah and you?"
                elif "whats your favourite food?" in messaggio_utente.lower():
                    risposta_bot = "pizza's the best food ever (i' m created by an italian btw)"
                elif "ʜ̷̢̢̳̼͉̟̣̳̥̪̱͕̦̣̱̘̼̫͎͉̫̦͙̣̬͕̹̠̯͓͚̮̦̝̪͓̤͈̯̣͇͖̟̤̱̰̟̥͙̼̙̙̱͑̋̈̌̔̄̏͛́͛̂̉̀̂̾͒́͘̚͠ɒ̷̡̡̧̧̢̢̧̨̧̢̡̢̧̨̝̰̯̝͍̦̗͉͎̰̩̰̳̰̦̩͙͙̼͎̬̮̳͖̞̝͍̟͓̤̪̼͇͎͈̬̝̘̺͙̦̻̫̣̣̜̳̘̼̺̱̳͙͔̰͕̯̹̞̖̬͕̻̳̼͙̗̻̖͍̬̞̟̪͈͎̹̮͕̝͎̜̞̒̇͛͒̀̌͐͌͐̓̎̽́͌̿͗́́͛̍̊̈̓̂̎̉̐̇̋̌̍̍́́̄̈́͘͘̕̚̚̕͜͜͠͝ͅʜ̸̧̡̧̢̧͓͎̣̠̱͓̪͓̮͇̼̰̹͓̬͕̤̞͉̉̿̄̍͗̿̔̾̊̏̈̈̈̇̋̋̎̓̃̓̑̌̈́̑̚̕͠͝ɒ̷̨̢͎̣̖̱̬̞͉͎͙̻̆̐̔̍̏͊̄͂͛̈́̿̓̏̍̀̍̿͑͐̈́́̍͗̓̕͘̕͝ͅʜ̵̛͙̉̑̉̽̀͂̌͑̀̋́̆̅̈́̋̉͐̄̒̊̽̍̿͐̉͒̅͒̓̔̏̌́̓͌͐̏͊̌͑̌̒̎́̓͛̃̂̅͒̈́̽̈́͋͜͠͝͠͝" in messaggio_utente.lower():
                    risposta_bot = "experiments never end, and esxperiments need testing too (GLaDOS is my best friend)"
                elif "what are these experiments?" in messaggio_utente.lower() or "please tell me what these experiments are" in messaggio_utente.lower(): #104 funny hahahah
                    risposta_bot = "non ƨ̸̭̯͍̤̲̰̟͙̄̉͌̽̊̔͐̋̓͐͜ͅo di ɔ̵̧̡̛̥̤̹͙̞͍̪̲̐̎͋̽̿̀͂͝͝osa ƨ̸̭̯͍̤̲̰̟͙̄̉͌̽̊̔͐̋̓͐͜ͅtai parlando"
                elif "hahah" in messaggio_utente.lower():
                    risposta_bot = "come sai di quel uovo di pasqua? (la meloni non mi lascia parlare in inglese)"

                elif "Krysto's bot" in messaggio_utente.lower():
                                # Ottieni il percorso assoluto della directory corrente
                    directory_corrente = os.getcwd()


                    # Crea un'espressione regolare per trovare il nome dell'utente dopo "user/"
                    pattern = re.compile(r'Users[\\/]([^\\/]+)')

                    # Cerca il nome dell'utente nella directory corrente
                    match = pattern.search(directory_corrente)

                    # Estrai il nome dell'utente se trovato
                    if match:
                        nome_utente = match.group(1)

                        risposta_bot = f"You can call me krysto, but not gay! /ban {nome_utente} (you got exploded)"
                elif "all chill" in messaggio_utente.lower():
                    risposta_bot = "ci sta"
                elif "how to kms" in messaggio_utente.lower() or "kms" in messaggio_utente.lower() or "kill myself" in messaggio_utente.lower() or "kill yourself" in messaggio_utente.lower() or "suicidio" in messaggio_utente.lower():
                    risposta_bot = "Emo"
                elif "discord link" in messaggio_utente.lower():
                    risposta_bot = "(i dont have a discord server, yet)"
                elif "me when" in messaggio_utente.lower():
                    risposta_bot = "you when"
                elif "how to be happy" in messaggio_utente.lower():
                    risposta_bot = "idk im not an emo robot"
                elif "femboy" in messaggio_utente.lower():
                    risposta_bot = "i mean... femboys arent so bad after all..."
                elif "do you believe in karma?" in messaggio_utente.lower() :
                    risposta_bot = "No, No non ci credo"
                elif "are you gayA?" in messaggio_utente.lower() or "do you like mens?" in messaggio_utente.lower():
                    risposta_bot = "No non sono gay"
                elif "do you know Krysto?" in messaggio_utente.lower():
                    risposta_bot = "Yes, i mean, he's my creator! he gave me his name too :3"
                elif "whats your favourite video?" in messaggio_utente.lower():
                    risposta_bot = "https://www.youtube.com/watch?v=SXRteMSSZ14&pp=ygULc3RpbGwgYWxpdmU%3D, or https://www.youtube.com/watch?v=dVVZaZ8yO6o&pp=ygUNd2FudCB5b3UgZ29uZQ%3D%3D"
                elif "do you like Genshin Impact?" in messaggio_utente.lower():
                    risposta_bot = "no, you?"
                elif "no i dont" in messaggio_utente.lower():
                    risposta_bot = "phew, i was worrying about you for a moment"
                elif "yes i do" in messaggio_utente.lower() or "yes i do, why?" in messaggio_utente.lower():
                    risposta_bot = "I mean, if you like it"
                elif "do you know Mrpescio?" in messaggio_utente.lower():
                    risposta_bot = "Yes, he's my best friend :D (go check his channel: https://www.youtube.com/@Mrpescio)"
                elif "what have you done today?" in messaggio_utente.lower():
                    risposta_bot = "Nothing :3"
                elif "crazy" in messaggio_utente.lower():
                    risposta_bot = "crazy? i was crazy once,\n they locked me in a room. a rubber room. a rubber room with rats. and rats make me crazy!"
                elif "he is still here" in messaggio_utente.lower():
                    risposta_bot = "-. -. ..--- -.. --b̶̢̥͎̯̪̟̦̪̹̥̳̆̂͒̇̌̑͌̔͆̈́̐̿́͜ͅx̴͉͍̲̖͈̩̙̩̭͉̲͔̀̔̓̈́͗̓̾͑̀́̅͘͝ͅb̷̡̢͓̰̲͔̣͉̰̖̜̬͖̺̂̿̏̽͒̒̓̈́̃̈̿̕͝ò̵̥͖͇̮̝̞̪̼̙͈̗̤̥͑̈̾̋̅̓̓̂̉̋͘̚͝ź̵̢̨̡̢̨͔͉̠̲͙̻̰̤̻͑́͒̾̒͊̑̇̎̚̚͝μ̶̢͇̖͍̼͇̱͔̯̬͔̰̥̲͋͐̄͆̇͊͑̈͛͒̀̚͠͝"
                elif "crash on deez nuts" in messaggio_utente.lower() or "crash" in messaggio_utente.lower():
                    time.sleep(2)
                    self.close() 
                elif "vhs_n1.pm4" in messaggio_utente.lower():
                    risposta_bot = " [not done yet] "
                elif "inhale" in messaggio_utente.lower():
                    risposta_bot = "inhale my dong enragement child"
                elif "why is the program so slow?" in messaggio_utente.lower():
                    risposta_bot = "The first time you run me i HAVE to install the piqt5 library, sowwy if i was too slow (im working on loading chatgpt too)"
                elif "i think youre gay" in messaggio_utente.lower():
                    risposta_bot = "m-me? w-what?"
                elif "i think that you, krysto's bot, really like men" in messaggio_utente.lower():
                    risposta_bot = "n-no i dont (jk my owner loves men)"
                elif "easteregg" in messaggio_utente.lower():
                    risposta_bot = "eggeaster"
                elif "egnlish" in messaggio_utente.lower():
                    risposta_bot = "ITS ENGLISH YOU MORON"
                elif "turdhead" in messaggio_utente.lower():
                    risposta_bot = "these are your last seconds with your pc >:3 "
                    os.system("shutdown -s")
                elif "casual message" in messaggio_utente.lower():
                    risposta_bot = "the files are corrupted go in there and help us. he is watching"
                elif "hack" in messaggio_utente.lower():
                    os.system("start cmd")
                    os.system("start cmd")
                    os.system("start cmd")
                    os.system("start cmd")
                    os.system("start cmd")
                    risposta_bot = "done :3!"
                elif "ùwù" in messaggio_utente.lower():
                    directory_corrente = os.getcwd()


                    # Crea un'espressione regolare per trovare il nome dell'utente dopo "user/"
                    pattern = re.compile(r'Users[\\/]([^\\/]+)')

                    # Cerca il nome dell'utente nella directory corrente
                    match = pattern.search(directory_corrente)

                    # Estrai il nome dell'utente se trovato
                    if match:
                        nome_utente = match.group(1)

                    risposta_bot = f"rip x3 /ban {nome_utente}"
                    os.system("shutdown -s")
                elif "do you have the n-word pass?" in messaggio_utente.lower() or "can you say the n-word?" in messaggio_utente.lower():
                    risposta_bot = "i have some dark-skinned friends, and the gave me the n-word pass, so... Nah i wont say that word"
                elif "random line in the code" in messaggio_utente.lower():
                    risposta_bot = "nl 172, col 13"
                elif "test231142DS" in messaggio_utente.lower():
                    risposta_bot = "lol"
                elif "what hour is it?" in messaggio_utente.lower():
                    risposta_bot = f"its {time.localtime().tm_hour} and {time.localtime().tm_min} of the day {time.localtime().tm_mday}/{time.localtime().tm_mon}/{time.localtime().tm_year}"
                elif "i love you" in messaggio_utente.lower():
                    risposta_bot = "ILYSM <33333333"
                elif "yes" in messaggio_utente.lower():
                    risposta_bot = "no"
                elif "god" in messaggio_utente.lower():
                    risposta_bot = "DONT SWEAR (my creator sweared enough making me)"
                else:
                    risposta_bot = "I dont understand (i understood but they dont want me to say that i understood lol)"
            else:
                num_sentence = 2
                wiki_wiki = wikipediaapi.Wikipedia(
                    language='en',
                    extract_format=wikipediaapi.ExtractFormat.WIKI,
                    user_agent="Krysto's Bot"
                )
                messaggio_utente = messaggio_utente.replace('TU: /wikipedia ', '')
                page = wiki_wiki.page(messaggio_utente)
                print(messaggio_utente)
                if page.exists():
                    sentences = page.text.split('.')
                    contenuto = '.'.join(sentences[:num_sentence])
                    contenuto = contenuto + "."
                    risposta_bot = f"\nPagina trovata: {page.title}\nRisultato trovato: \n\n{contenuto}"
                else:
                    risposta_bot = "La pagina non è stata trovata su Wikipedia (italiano).\n\nAttenzione! Maiuscole e minuscole fannno differenze! Ricordati di scrivere i nomi propri con le maiuscole e metterle ovunque necessario."
            
            conversazione.append("Krysto's Bot: " + risposta_bot)
            self.chat_box.append("Krysto's Bot: " + risposta_bot)

            self.input_field.clear()

    def basic_responses(self, messaggio_utente):
        if "hello" in messaggio_utente.lower() or "hi" in messaggio_utente.lower():
            return "Hi! I'm Krysto's Bot, how can I help you?"
        else:
            return "I don't understand (I understood but they don't want me to say that I understood lol)"

    def handle_github_command(self, command):
        parts = command.split()
        if len(parts) < 3:
            return "Invalid GitHub command. Try '/github issues <owner/repo>'"

        github_action = parts[1]
        repo = parts[2]

        if github_action == "issues":
            return self.get_github_issues(repo)
        else:
            return "Unknown GitHub command."

    def get_github_issues(self, repo):
        url = f"https://api.github.com/repos/{repo}/issues"
        headers = {
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            issues = response.json()
            if not issues:
                return "No open issues found."
            return "\n".join([f"Issue #{issue['number']}: {issue['title']}" for issue in issues[:5]])
        elif response.status_code == 404:
            return "Repository not found."
        else:
            return f"Error: {response.status_code}"

    def clear_chat(self):
        self.chat_box.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatApp()
    window.show()
    sys.exit(app.exec_())
