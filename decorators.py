from datetime import datetime


def log_deco(old_function):
    def new_foo(*args, **kwargs):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")



        result = old_function(*args, **kwargs)

        with open("log.txt", "a") as log_file:
            log_file.write(f"{dt_string} -Запущена функция {old_function.__name__} c аргументами {args}-{kwargs}."
                           f" Функция вернула результат {result} \n")




        return result

    return new_foo


def log_deco_param(log_file_name):
    def _log_deco(old_function):
        def new_foo(*args, **kwargs):
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

            result = old_function(*args, **kwargs)

            with open(log_file_name, "a") as log_file:
                log_file.write(f"{dt_string} -Запущена функция {old_function.__name__} c аргументами {args}-{kwargs}."
                               f" Функция вернула результат {result} \n")

            return result

        return new_foo

    return _log_deco
