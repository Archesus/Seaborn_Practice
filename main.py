import seaborn as sns

datasets = sns.get_dataset_names()
# print(datasets)

penguins = sns.load_dataset("penguins")
# print(penguins["island"].value_counts())

sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g")