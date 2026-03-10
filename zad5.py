filename = "LV1/SMSSpamCollection.txt"

ham_word_count = 0
spam_word_count = 0
ham_count = 0
spam_count = 0
spam_exclamation_count = 0

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
       
        line = line.strip()
        
        if not line:
            continue
        
        
        label, message = line.split('\t', 1)
        
        
        words = message.split()
        word_count = len(words)
        
        if label == "ham":
            ham_count += 1
            ham_word_count += word_count
        elif label == "spam":
            spam_count += 1
            spam_word_count += word_count
            
            if message.endswith("!"):
                spam_exclamation_count += 1

avg_ham = ham_word_count / ham_count if ham_count > 0 else 0
avg_spam = spam_word_count / spam_count if spam_count > 0 else 0

# Ispis rezultata
print("Prosječan broj riječi u ham porukama:", avg_ham)
print("Prosječan broj riječi u spam porukama:", avg_spam)
print("Broj spam poruka koje završavaju uskličnikom:", spam_exclamation_count)