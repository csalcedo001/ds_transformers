from data_generator import DataGenerator

dg = DataGenerator(push_prob=0.5)

data = dg.sample()

print(data)