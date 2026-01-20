"""
Experiment 01: Simple ML Pipeline (Concept-Level)

This file demonstrates the logical flow of a machine learning pipeline
without focusing on model complexity.

Goal: Understand system structure, not algorithms.
"""

def ingest_data():
    print("Step 1: Ingesting data...")
    # Simulated data
    data = [100, 200, 300, 400, 500]
    return data


def preprocess_data(data):
    print("Step 2: Preprocessing data...")
    # Simple transformation
    processed = [x / 100 for x in data]
    return processed


def train_model(processed_data):
    print("Step 3: Training model...")
    # Simulated "model"
    model = sum(processed_data) / len(processed_data)
    return model


def evaluate_model(model):
    print("Step 4: Evaluating model...")
    # Fake evaluation metric
    score = round(model * 10, 2)

    return score


def run_pipeline():
    data = ingest_data()
    processed_data = preprocess_data(data)
    model = train_model(processed_data)
    score = evaluate_model(model)

    print("Step 5: Output")
    print(f"Final evaluation score: {score}")


if __name__ == "__main__":
    run_pipeline()

