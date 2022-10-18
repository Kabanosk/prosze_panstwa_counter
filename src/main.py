#!/usr/bin/python3

import speech_recognition as sr
import re


def count_prosze_panstwa_occurences(text):
    prosze_panstwa_regex = re.compile("proszę państwa",
                                      re.IGNORECASE | re.UNICODE)
    return len(prosze_panstwa_regex.findall(text))


def listen_to_the_lecture():
    prosze_panstwa_counter = 0
    text = ""

    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 400
    recognizer.pause_threshold = 0.5

    while True:
        with sr.Microphone() as source:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language='pl-PL')
                prosze_panstwa_counter += count_prosze_panstwa_occurences(text)
            except sr.UnknownValueError:
                pass
            except KeyboardInterrupt:
                exit()
            except:
                print("A recognizer exception occured.")
            finally:
                print("Current 'PROSZĘ PAŃSTWA COUNTER' wynosi",
                      prosze_panstwa_counter)


if __name__ == "__main__":
    listen_to_the_lecture()
