![Landing Page](https://github.com/ilhaammulia/travelyou-ai/blob/master/image.png)

# LLM + Google Maps Search

This project demonstrates integrating a **local LLM** (via [Open WebUI](https://github.com/open-webui/open-webui)) with the **Google Maps API**.  
Users can enter natural language prompts (e.g. *"Where to eat cheap nasi goreng near Malioboro tonight"*) and receive a list of relevant places with links to Google Maps.

---

## Features

- **LLM Prompting**: Natural language queries are passed to the local LLM.
- **Google Maps Integration**:
  - Place search
  - Open in Google Maps directly
- **Backend API**: Python (Flask) with **MVT + Repository Pattern** for clean separation of concerns.
- **Frontend**: Simple HTML/JS frontend.
- **Rate Limiting Middleware**: Custom implementation to protect API usage.
- **Best Practices**:
  - API keys secured with environment variables.
  - Usage limits enforced via middleware.
  - Repository layer for clean data access abstraction.

---

## Prerequisite

- **Open WebUI** runs locally on port `3001`.
- You have created a new **Google Cloud project** with a **Maps API key** (free tier credits available).
- The LLM is already connected to Open WebUI (you can choose any supported model, e.g. OpenAI, Ollama, Llama.cpp).


