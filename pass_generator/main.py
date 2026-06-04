from pass_generator.generator import PasswordGenerator


def main():
    """Главная функция программы с главным циклом."""
    generator = PasswordGenerator()

    while True:
        print("\n--- Новая попытка генерации ---")
        generator.get_user_settings()

        password = generator.generate_password()

        if password:
            print("\nВаш новый пароль:")
            print(password)
        else:
            print("\nПароль не был сгенерирован. Пожалуйста, проверьте введенные параметры.")

        repeat = input("\nСгенерировать еще один пароль? (y/n): ").strip().lower()
        if repeat != 'y':
            print("Завершение работы. До свидания!")
            break


if __name__ == "__main__":
    main()