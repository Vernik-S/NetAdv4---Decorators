from request import get_q
from decorators import log_deco, log_deco_param

get_q_log = log_deco(get_q) #декорированная функция под стандартное имя файла с логами

print(get_q_log(1))

log_deco_file = log_deco_param("random_name.txt") #генератор декоратора под произвольное название файла

get_q_log2 = log_deco_file(get_q) #декорированная функция под произвольное имя файла

print(get_q_log2(2))