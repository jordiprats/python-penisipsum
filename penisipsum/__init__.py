import random

penisnames = [
  "penis",
  "escrotum",
  "glandum",
  "pollamen",
  "pollamum",
  "rabaken",
  "rabakum",
  "vergum",
  "huevum",
  "testiculum",
  "testiculae",
  "escrotae",
  "prepucium",
  "gonorreum",
  "gonorrae",
  "vergae",
  "vergum",
  "nabum",
  "falum",
  "cum",
  "perineum",
  "perinae",
  "frenillum",
  "perialanum",
  "mastilum",
  "pollenae",
  "membrum"
]

adjectius = [
  "tochum",
  "sifilosum",
  "balanitis",
  "maximus",
  "magnanimus",
  "magnificus",
  "torticum",
  "durum",
  "blandicum",
  "blandicae",
  "gustosum",
  "apetitosus",
  "minim",
  "desinflatum",
  "penosum",
  "excelsus",
  "magicum",
  "divinum",
  "divinidorum",
  "microlae",
  "fimosidamus",
  "cipotum",
  "pichum",
  "smegmum"
]

nexes = [
  "sit",
  "amet",
  "sed",
  "do",
  "ut",
  "anus",
  "et",
  "ad",
  "quis",
  "nisi",
  "ex",
  "ea",
  "aute",
  "in",
  "eu",
  "sint",
  "sunt",
  "qui",
  "est"
]

def sentence(words=15, base_words="Penis ipsum", capitalize=True, add_period=True):
    message=[]
    if len(base_words.split()) > 0:
      message.append(base_words)
    for i in range(0, words-len(base_words.split())):
      randword=random.randint(0,i)
      if randword%2 == 0:
        message.append(nexes[random.randint(0,len(nexes)-1)])
      elif randword%3 == 0:
        message.append(adjectius[random.randint(0,len(adjectius)-1)])
      else:
        message.append(penisnames[random.randint(0,len(penisnames)-1)])
    retstr=' '.join(message)
    if capitalize:
      retstr=retstr.capitalize()
    if add_period:
      retstr+='.'
    return retstr

def paragraph(sentences=5, max_words_per_sentence=15, min_words_per_sentence=3):
    message=[]
    message.append(sentence(random.randint(0, max_words_per_sentence)))
    for i in range(0,sentences):
      message.append(sentence(random.randint(min_words_per_sentence, max_words_per_sentence),'', True, True))
    return ' '.join(message)
