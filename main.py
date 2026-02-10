from src.train import train
from src.evaluate import evaluate

if __name__ == "__main__":
    model, X_test, y_test = train()
    evaluate(model, X_test, y_test)
