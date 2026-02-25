client Nebius {
  provider openai

  options {
    base_url "https://api.studio.nebius.ai/v1"
    model "nvidia/Nemotron-Nano-V2-12b"
    temperature 0
    top_p 0.9
  }
}
