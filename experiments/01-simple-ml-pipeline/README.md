# Experiment 01: Simple ML Pipeline (Concept-Level)

This experiment documents a simple machine learning pipeline from data ingestion to evaluation.

The goal is not to train a complex model, but to clearly understand how ML systems are structured.

## Pipeline Overview

1. Data ingestion
2. Data preprocessing
3. Model training
4. Model evaluation
5. Output and interpretation

## Data

- Source: Synthetic or small sample dataset
- Type: Tabular data
- Size: Small (designed for fast iteration)

## Model Choice

- Simple supervised learning model
- Chosen for interpretability rather than performance

## Evaluation

- Basic evaluation metrics
- Focus on understanding results rather than optimization

## System Thinking Notes

- Where data validation would occur
- Where model monitoring would be added in production
- How this pipeline could evolve into a batch or API-based system

## Status

Concept documented.  
Implementation to be added incrementally.

---

Built under UStack Solutions.
## AWS Mapping (Conceptual)

This experiment maps conceptually to the following AWS services:

- **Data ingestion**: Amazon S3, AWS Glue
- **Data preprocessing**: SageMaker Processing Jobs, AWS Glue DataBrew
- **Model training**: Amazon SageMaker Training Jobs
- **Model evaluation**: SageMaker Processing
- **Deployment (future)**: SageMaker Endpoints or Batch Transform
- **Monitoring (future)**: SageMaker Model Monitor, Amazon CloudWatch
The following steps outline how this concept-level experiment will evolve into a more complete ML workflow:
## Next Steps

- Add a small synthetic dataset for hands-on validation
- Implement basic preprocessing and validation logic
- Extend the pipeline to support batch inference
- Explore orchestration using SageMaker Pipelines
