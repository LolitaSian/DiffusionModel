from datasets import load_dataset

# load dataset from the hub
dataset = load_dataset("fashion_mnist")

print(dataset['train'][0])