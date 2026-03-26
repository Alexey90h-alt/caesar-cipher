def caesar_cipher():
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    print("🔐 Добро пожаловать в Шифратор Цезаря!")
    action = input("Что делаем? (зашифровать/расшифровать): ").lower()
    text = input("Введите текст на русском: ").lower()
    shift = int(input("Введите число (сдвиг): "))

    # Если нужно расшифровать, просто делаем сдвиг отрицательным
    if action == 'расшифровать':
        shift = -shift

    result = ""

    for char in text:
        if char in alphabet:
            # Находим текущий индекс буквы
            index = alphabet.find(char)
            # Вычисляем новый индекс с учетом сдвига
            new_index = (index + shift) % len(alphabet)
            result += alphabet[new_index]
        else:
            # Если это пробел или знак препинания, оставляем как есть
            result += char

    print(f"✅ Результат: {result}")

if __name__ == "__main__":
    caesar_cipher()