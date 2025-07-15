import pandas as pd
import matplotlib.pyplot as pit

tabela = pd .DataFrame ({
    'Idade': [20, 23, 45, 31, 32],
    'nome': ['Robeto', 'Katia', 'Joao', 'Ronaldo', 'Jessica']
})

pit.hist (tabela['Idade'])