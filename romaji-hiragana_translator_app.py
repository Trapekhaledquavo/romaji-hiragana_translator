romaji_to_hiragana = {
    "a": "あ",
    "i": "い",
    "u": "う",
    "e": "え",
    "o": "お",
    "ka": "か",
    "ki": "き",
    "ku": "く",
    "ke": "け",
    "ko": "こ",
    "kya": "きゃ",
    "kyu": "きゅ",
    "kyo": "きょ",
    "sa": "さ",
    "shi": "し",
    "su": "す",
    "se": "せ",
    "so": "そ",
    "sha": "しゃ",
    "shu": "しゅ",
    "sho": "しょ",
    "ta": "た",
    "chi": "ち",
    "tsu": "つ",
    "te": "て",
    "to": "と",
    "cha": "ちゃ",
    "chu": "ちゅ",
    "cho": "ちょ",
    "na": "な",
    "ni": "に",
    "nu": "ぬ",
    "ne": "ね",
    "no": "の",
    "nya": "にゃ",
    "nyu": "にゅ",
    "nyo": "にょ",
    "ha": "は",
    "hi": "ひ",
    "fu": "ふ",
    "he": "へ",
    "ho": "ほ",
    "hya": "ひゃ",
    "hyu": "ひゅ",
    "hyo": "ひょ",
    "ma": "ま",
    "mi": "み",
    "mu": "む",
    "me": "め",
    "mo": "も",
    "mya": "みゃ",
    "myu": "みゅ",
    "myo": "みょ",
    "ya": "や",
    "yu": "ゆ",
    "yo": "よ",
    "ra": "ら",
    "ri": "り",
    "ru": "る",
    "re": "れ",
    "ro": "ろ",
    "rya": "りゃ",
    "ryu": "りゅ",
    "ryo": "りょ",
    "wa": "わ",
    "wi":"ゐ",
    "we":"ゑ",
    "wo":"を",
    "ga": "が",
    "gi": "ぎ",
    "gu": "ぐ",
    "ge": "げ",
    "go": "ご",
    "gya": "ぎゃ",
    "gyu": "ぎゅ",
    "gyo": "ぎょ",
    "za": "ざ",
    "ji": "じ",
    "zu": "ず",
    "ze": "ぜ",
    "zo": "ぞ",
    "ja": "じゃ",
    "ju": "じゅ",
    "jo": "じょ",
    "da": "だ",
    "de": "で",
    "do": "ど",
    "ba": "ば",
    "bi": "び",
    "bu": "ぶ",
    "be": "べ",
    "bo": "ぼ",
    "bya": "びゃ",
    "byu": "びゅ",
    "byo": "びょ",
    "pa": "ぱ",
    "pi": "ぴ",
    "pu": "ぷ",
    "pe": "ぺ",
    "po": "ぽ",
    "pya": "ぴゃ",
    "pyu": "ぴゅ",
    "pyo": "ぴょ",
    "n": "ん",
    " ": " ",
    "\n": "\n",
    "k": "っ",
    "s": "っ",
    "t": "っ",
    "h": "っ",
    "f": "っ"
}

def translate_line(line): #Translate function definition
    hiragana_translation = ""
    syllables = []

    i = 0
    line = line.lower()  # Convert input to lowercase
    while i < len(line): # Remove extra spaces and split the input text into romaji syllables
        found = False
        for length in range(5, 0, -1): # Matches longer syllables first
            syllable = line[i:i + length]
            if syllable in romaji_to_hiragana:
                syllables.append(syllable)
                i += length
                found = True
                break
        if not found:
            print("Invalid romaji syllable found:", line[i])
            return

    # Translate each romaji syllable to hiragana
    for syllable in syllables:
        hiragana_translation += romaji_to_hiragana[syllable]

    return hiragana_translation

def translate(input_text):
    lines = input_text.split('\n')  # Split input into lines
    for line in lines:
        hiragana_translation = translate_line(line)
        if hiragana_translation:
            print(hiragana_translation)
        else:
            print("No translation found")

# Input text with multiple lines and paragraphs
# Replace the inserted input with what you want to translate
input_text = """Hanron nado iranai
Negatte shimatta anata no make sa
Nagai nemuri no tabi no hajimari da"""

translate(input_text)
