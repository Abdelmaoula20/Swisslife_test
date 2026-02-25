# **Technical Test AI Swiss Life- Data Scientist**

**Candidate: Abdelmaoula Essabbahi**

------------------------------------------------------------------------

## 1. Overview

This project implements an API addressing two LLM-powered use cases:

1.  **Text Classification**
2.  **Form Completion (Structured Data Extraction)**

The system is built using:

-   FastAPI (API layer)
-   BAML (structured LLM generation)
-   UV (dependency & environment management)
-   Nebius Inference API (LLM provider)

The implementation focuses on:

-   Structured generation
-   Robustness
-   Production-ready architecture
-   Error handling
-   Observability
-   Deterministic behavior

------------------------------------------------------------------------

## 2. Architecture

```
project/
│
├── app/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   └── models/
│
├── baml_src/
│   ├── clients.baml
│   ├── classification.baml
│   └── form_completion.baml
│
├── baml_client/
│
└── README.md
```

Design principles:

-   Clear separation of concerns
-   LLM logic isolated in BAML
-   Business logic in services layer
-   Strong schema validation
-   Defensive API design

------------------------------------------------------------------------

## 3. Installation

### Install UV

curl -Ls https://astral.sh/uv/install.sh \| sh

### Install dependencies

uv sync

------------------------------------------------------------------------

## 4. Environment Variables

Create a .env file:

OPENAI_API_KEY=api_key\
OPENAI_BASE_URL=https://api.studio.nebius.ai/v1

------------------------------------------------------------------------

## 5. Generate BAML Client

uv run baml generate

------------------------------------------------------------------------

## 6. Run the API

uv run uvicorn app.main:app --reload

Swagger available at:

http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## 7. Use Case 1 -- Text Classification

### Endpoint

POST /classify

### Input Example

{ "text": "I was charged twice and my connection is unstable.",
"themes": \[ { "title": "Technical support", "description": "Tech
issues" }, { "title": "Billing", "description": "Payment issues" } \] }

### Output Example

{ "model_reasoning": "...", "chosen_theme": { "title": "Billing",
"description": "Payment issues" }, "confidence": 1.0 }

### Bonus 1 -- Probabilistic Classification

-   Multiple parallel LLM calls
-   Majority vote aggregation
-   Empirical confidence score

Note: In constrained classification tasks, the model behaves
near-deterministically, often resulting in confidence = 1.0. This
reflects strong convergence rather than instability.

------------------------------------------------------------------------

## 8. Use Case 2 -- Form Completion

### Endpoint

POST /form-completion

### Output Example

{ "personal_info": { "first_name": "John", "last_name": "Doe", "gender":
null }, "contact_info": { "email": "johndoe@example.com", "phone": null,
"preferred_contact_method": "Email", "call_reasons": null } }

------------------------------------------------------------------------

## 9. Robustness Features

-   Strict JSON schema enforcement via BAML
-   Enum validation
-   Retry mechanism on transient LLM failures
-   Structured logging
-   Defensive error handling (500 / 503 / 422)

------------------------------------------------------------------------

## 10. Production Considerations

-   Temperature = 0 for deterministic behavior
-   Async parallel execution
-   Stateless API design
-   Prompt injection mitigation rules

------------------------------------------------------------------------

## 11. Conclusion

This implementation prioritizes:

-   Robustness
-   Determinism
-   Clean architecture
-   Structured LLM usage
-   Production-readiness

The probabilistic classification mechanism demonstrates understanding of
LLM stochastic behavior while maintaining enterprise-grade stability.
