import pandas as pd

features = pd.read_csv("data/features.csv")
test = pd.read_csv("data/test.csv")
train = pd.read_csv("data/train.csv")
stores = pd.read_csv("data/stores.csv")



train_data = pd.merge(train, stores)
train_data = pd.merge(merged_train , features)

test_data = test.merge(test.merge(stores, how='left', sort=False))
test_data = test_data.merge(test_data.merge(features, how='left', sort=False))


train_data.to_csv("data/train_data.csv", index = False)
test_data.to_csv("data/test_data.csv", index = False)
