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

```json
{
    "text": "I am calling because I have a problem with my internet connection",
    "themes": [
        {
            "title": "Technical support",
            "description": "The customer is calling for technical support"
        },
        {
            "title": "Billing",
            "description": "The customer is calling for billing issues"
        },
        {
            "title": "Refund",
            "description": "The customer is calling for a refund"
        }
    ]
}
```

### Output Example

```json
{
    "model_reasoning": "This text is about technical support, therefore the chosen theme is 'Technical support'.",
    "chosen_theme": {
        "title": "Technical support",
        "description": "The customer is calling for technical support",
        "confidence":1.0
    }
}
```

### Bonus 1 -- Probabilistic Classification

-   Multiple parallel LLM calls
-   Majority vote aggregation
-   Empirical confidence score

------------------------------------------------------------------------

## 8. Use Case 2 -- Form Completion

### Endpoint

POST /form-completion

### Output Example

```json
{
  "personal_info": {
    "first_name": "John",
    "last_name": "Doe",
    "gender": null
  },
  "contact_info": {
    "email": "johndoe@example.com",
    "phone": null,
    "preferred_contact_method": "Email",
    "call_reasons": null
  }
}
```
------------------------------------------------------------------------

