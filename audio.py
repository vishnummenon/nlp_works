import speech_recognition as sr
from text_summarizer import FrequencySummarizer
import nltk

r = sr.Recognizer()
r.pause_threshold = 0.5
harvard = sr.AudioFile('test.wav')
with harvard as source:
    #r.adjust_for_ambient_noise(source,duration=0.5)
    audio = r.record(source)
    out = r.recognize_google(audio, language ='en-IN')
    #out = r.recognize_wit(audio,'EAIKHTMGQI7I37Z3UCVR3AGRCWBDDEZ6')
n = nltk.tokenize.punkt.PunktSentenceTokenizer()
abc = n.sentences_from_text(out)
print (abc)
'''
fs = FrequencySummarizer()
final_summary = fs.summarize(out, 3)
print (" ".join(final_summary))
'''
