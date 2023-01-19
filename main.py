from data_generator import DataGenerator

dg = DataGenerator(
    push_prob=0.5,
    min_seq_len=10,
    is_error_free=False,
)

data = dg.sample()

print(data)