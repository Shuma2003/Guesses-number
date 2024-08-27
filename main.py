import random

def play_game():
  """Функция, запускающая игру"""

  number = random.randint(1, 100)
  attempts = 0
  max_attempts = 7

  print("Добро пожаловать в игру 'Угадай число'!")
  print("Я загадал число от 1 до 100. У вас есть 7 попыток.")

  while attempts < max_attempts:
    try:
      guess = int(input(f"Попытка {attempts + 1}: Введите число: "))
    except ValueError:
      print("Некорректный ввод. Введите целое число.")
      continue

    attempts += 1

    if guess < number:
      print("Слишком мало!")
    elif guess > number:
      print("Слишком много!")
    else:
      print(f"Поздравляю! Вы угадали число {number} за {attempts} попыток!")
      return

  print(f"У вас закончились попытки. Загаданное число было {number}.")

if __name__ == "__main__":
  play_game()
