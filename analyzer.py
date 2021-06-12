from os import listdir
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

pd.set_option("display.max_columns", None)

print(*[file_name.split(".")[0] for file_name in listdir("opinions")], sep ="\n")
product_id = input('Podaj kod produktu: ')


reviews = pd.read_json(f"opinions/{product_id}.json")

reviews.stars = reviews.stars.map(lambda stars: float(stars.split("/")[0].replace(",",".")))

reviews_counts = len(reviews.index)

pros_count = reviews.pros.astype(bool).sum()
cons_count = reviews.cons.astype(bool).sum()

average_score =  reviews.stars.mean().round(2)


stars = reviews.stars.value_counts().reindex(np.arange(0,5.5,0.5), fill_value = 0)
stars.plot.bar(color="red")
plt.title("gwiazdki")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
#plt.show()
plt.savefig(f"plots/{product_id}.png")
plt.close()