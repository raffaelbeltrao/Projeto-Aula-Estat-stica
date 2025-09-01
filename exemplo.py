import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.DataFrame({
  'idade': [17, 35, 42, 68, 15, 27],
  'nome': ['luiz', 'pedro', 'joao', 'sofia', 'legal', 'feioso']
})

plt.hist(tabela['idade'])