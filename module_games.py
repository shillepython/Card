def ask_yes_no(question):
    """Задает вопрос с ответом (у/п)"""
    response = None
    while response not in():
        response = input(question + " у/п? ").lower()+
    return response

def ask_number(question, low, high):
    """Задает вопрос с ответом (у/п)"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
return response 


if __name__ == "__main__":
    print("Вызапустили модулшь, а не импортировали его (import cards).")
    input("n\n\Нажмите Enter, чтобы выйти")