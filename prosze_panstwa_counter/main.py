import speech_recognition as sr


def prosze_panstwa_conting(text):
    counter = 0
    for i in range(len(text)):
        if text[i:i + 14].lower() == "proszę państwa":
            counter += 1
    return counter


def listening_the_lecture():
    prosze_panstwa_counter = 0
    text = ''
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language='pl-PL')
            except: pass
            prosze_panstwa_counter += prosze_panstwa_conting(text)
            print(f"Current 'PROSZĘ PAŃSTWA COUNTER' wynosi {prosze_panstwa_counter}")


listening_the_lecture()
