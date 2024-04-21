from matplotlib import pyplot as plt
movies = ["annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "west Side Story"]
num_oscars = [5, 11, 3, 8, 10]

plt.bar(range(len(movies)), num_oscars)
plt.title("Meus filmes favoritos")
plt.ylabel("# of Academy Awards")
plt.xticks(range(len(movies)),movies)
plt.show()

