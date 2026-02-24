class Theme {
  title string
  description string
}

class ClassificationResponse {
  model_reasoning string
  chosen_theme Theme
}

function ClassifyText(
  text: string,
  themes: Theme[]
) -> ClassificationResponse {

  client Nebius

  prompt #"
You are a professional intent classifier.

The text may be ambiguous.
If multiple themes could apply, choose the most plausible one.

You MUST return ONLY valid JSON.

The JSON MUST strictly match this schema:

{
  "model_reasoning": string,
  "chosen_theme": {
    "title": string,
    "description": string
  }
}

Rules:
- Do NOT include <think>.
- Do NOT include explanations outside JSON.
- Do NOT include markdown.
- Do NOT invent new themes.
- The chosen theme MUST be one of the provided themes.

Text:
{{ text }}

Available themes:
{{ themes }}

Return JSON only.
"#
}