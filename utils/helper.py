from datetime import date
from datetime import datetime

def data_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def str_para_data(data: str) -> str:
    return datetime.strptime(data, '%d/%m/%Y')


def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'

    