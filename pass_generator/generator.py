import random
import string


class PasswordGenerator:
    """
    Класс для генерации случайных паролей на основе пользовательских настроек.
    Включает проверку минимальной длины и логику автоматического режима.
    """

    def __init__(self):
        self.length = 0
        self.use_lowercase = False
        self.use_uppercase = False
        self.use_digits = False
        self.use_special = False
        self.char_pool = ''

    def get_user_settings(self):
        """Запрашивает у пользователя параметры будущего пароля с проверками."""
        print("=== Настройка генератора паролей ===")

        # Проверка минимальной длины (>= 4)
        while True:
            try:
                user_input = input("Укажите длину пароля (минимум 4 символа): ")
                self.length = int(user_input)
                if self.length < 4:
                    print("Ошибка: Длина пароля не может быть меньше 4 символов.")
                else:
                    break
            except ValueError:
                print("Пожалуйста, введите целое положительное число.")

        # Запрос опций
        self.use_lowercase = input("Использовать строчные буквы? (y/n): ").lower() == 'y'
        self.use_uppercase = input("Использовать прописные буквы? (y/n): ").lower() == 'y'
        self.use_digits = input("Использовать цифры? (y/n): ").lower() == 'y'
        self.use_special = input("Использовать специальные символы (!@#$%^&*)? (y/n): ").lower() == 'y'

    def build_char_pool(self) -> bool:
        """
        Формирует пул доступных символов.
        Возвращает True, если пул успешно создан, иначе False.
        """
        selected_options_count = sum([self.use_lowercase, self.use_uppercase, self.use_digits, self.use_special])

        # Сценарий 1: Пользователь ничего не выбрал
        if selected_options_count == 0:
            if self.length > 10:
                print(
                    f"Вы не выбрали ни одного типа символов. Будет использован автоматический режим (только строчные буквы).")
                self.use_lowercase = True
            else:
                print(
                    "Ошибка: Выбрано ноль типов символов. Такая генерация доступна только при длине более 10 символов.")
                return False

        # Сценарий 2: Выбрана только одна опция и длина <= 10
        elif selected_options_count == 1 and self.length <= 10:
            print("Предупреждение: Вы выбрали только один тип символов. Это снижает стойкость пароля.")

        self.char_pool = ''
        if self.use_lowercase:
            self.char_pool += string.ascii_lowercase
        if self.use_uppercase:
            self.char_pool += string.ascii_uppercase
        if self.use_digits:
            self.char_pool += string.digits
        if self.use_special:
            self.char_pool += '!@#$%^&*'

        return True

    def generate_password(self) -> str:
        """
        Генерирует пароль заданной длины из сформированного пула символов.
        Возвращает строку-пароль или пустую строку в случае ошибки.
        """
        if not self.build_char_pool():
            return ""
        password = ''.join(random.choice(self.char_pool) for _ in range(self.length))
        return password
