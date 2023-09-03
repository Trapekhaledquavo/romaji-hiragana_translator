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
    "  ": "  ",
    "   ": "   ",
    "    ": "    ",
    "\n": "\n"
}

def translate(input_text):
    hiragana_translation = ""
    syllables = []

    i = 0
    input_text = input_text.lower()  # Convert input to lowercase
    while i < len(input_text):
        found = False
        for length in range(5, 0, -1):
            syllable = input_text[i:i + length]
            if syllable in romaji_to_hiragana:
                syllables.append(syllable)
                i += length
                found = True
                break
        if not found:
            print("Invalid romaji syllable found:", input_text[i])
            return

    for syllable in syllables:
        hiragana_translation += romaji_to_hiragana[syllable]

    if hiragana_translation:
        print(hiragana_translation)
    else:
        print("No translation found")

word_to_translate = input("Type in the word to translate: ")
translate(word_to_translate)
