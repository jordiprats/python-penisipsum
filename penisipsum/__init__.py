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

def sentence(words=100, base_words="Penis ipsum"):
    message=[]
    message.append(base_words)
    for i in range(0, words-len(base_words.split())):
      randword=random.randint(0,i)
      if randword%2 == 0:
        message.append(nexes[random.randint(0,len(nexes)-1)])
      elif randword%3 == 0:
        message.append(adjectius[random.randint(0,len(adjectius)-1)])
      else:
        message.append(penisnames[random.randint(0,len(penisnames)-1)])
    return ' '.join(message)+'.'
