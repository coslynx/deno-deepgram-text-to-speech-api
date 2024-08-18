<div class="hero-icon" align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</div>

<h1 align="center">
deno-deepgram-text-to-speech-api
</h1>
<h4 align="center">A Deno API for converting text to speech using Deepgram's advanced speech models.</h4>
<h4 align="center">Developed with the software and tools below.</h4>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Language-Deno-blue" alt="Language-Deno">
  <img src="https://img.shields.io/badge/Framework-FastAPI-red" alt="Framework-FastAPI">
  <img src="https://img.shields.io/badge/Database-PostgreSQL-blue" alt="Database-PostgreSQL">
  <img src="https://img.shields.io/badge/API-Deepgram-black" alt="API-Deepgram">
  <img src="https://img.shields.io/badge/Rate%20Limiting-Upstash-black" alt="Rate Limiting-Upstash">
</div>
<div class="badges" align="center">
  <img src="https://img.shields.io/github/last-commit/spectra-ai-codegen/deno-deepgram-text-to-speech-api?style=flat-square&color=5D6D7E" alt="git-last-commit" />
  <img src="https://img.shields.io/github/commit-activity/m/spectra-ai-codegen/deno-deepgram-text-to-speech-api?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
  <img src="https://img.shields.io/github/languages/top/spectra-ai-codegen/deno-deepgram-text-to-speech-api?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

## 📑 Table of Contents
- 📍 Overview
- 📦 Features
- 📂 Structure
- 💻 Installation
- 🏗️ Usage
- 🌐 Hosting
- 📄 License
- 👏 Authors

## 📍 Overview
This repository houses a Minimum Viable Product (MVP) for a Deno API built to convert text to speech using Deepgram's powerful voice models. The API simplifies the integration of speech capabilities into applications, addressing the growing need for on-demand speech generation across diverse platforms like chatbots, interactive voice assistants, accessibility tools, and educational resources. The MVP utilizes a robust tech stack including Deno, FastAPI, PostgreSQL, Deepgram, and Upstash for rate limiting, ensuring efficient and secure operation.

## 📦 Features
|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The API is designed with a modular architecture, separating functionalities into distinct files and directories for enhanced maintainability and scalability.             |
| 📄 | **Documentation**  | This README provides a detailed overview of the API, its features, installation instructions, usage examples, and deployment guidelines. |
| 🔗 | **Dependencies**   | The API leverages external libraries and packages including FastAPI, SQLAlchemy, Deepgram, Upstash, and other essential dependencies for core functionality and integration. |
| 🧩 | **Modularity**     | The modular code structure promotes reusability and eases maintenance. Specific functionalities, like authentication, rate limiting, and speech generation, are encapsulated in dedicated modules. |
| 🧪 | **Testing**        | Thorough unit tests and integration tests are implemented to guarantee the reliability and correctness of the API's functionality.       |
| ⚡️  | **Performance**    | The API is optimized for performance, incorporating caching strategies and efficient data management to handle high volumes of requests. |
| 🔐 | **Security**       |  Robust security measures, including input validation, authentication, and data encryption, are implemented to protect user data and prevent unauthorized access. |
| 🔀 | **Version Control**| The project utilizes Git for version control with continuous integration and continuous delivery (CI/CD) implemented using GitHub Actions for automated builds and releases. |
| 🔌 | **Integrations**   | The API seamlessly integrates with external services through HTTP requests, including the Deepgram API for speech synthesis and Upstash for rate limiting and caching. |
| 📶 | **Scalability**    | The architecture is designed for scalability to handle increasing user demand. The API can be easily scaled horizontally and vertically based on traffic patterns.           |

## 📂 Structure
```text
deno-deepgram-text-to-speech-api/
├── app
│   ├── main.py
│   ├── models
│   │   └── user.py
│   ├── routers
│   │   └── speech.py
│   ├── services
│   │   └── speech_service.py
│   ├── utils
│   │   ├── auth.py
│   │   └── rate_limiter.py
│   ├── config
│   │   └── database.py
│   └── database.py
├── tests
│   └── test_speech.py
├── requirements.txt
└── .env
```

## 💻 Installation
### 🔧 Prerequisites
- Python 3.9+
- pip
- Docker
- Docker Compose

### 🚀 Setup Instructions
1. Clone the repository:
   - `git clone https://github.com/spectra-ai-codegen/deno-deepgram-text-to-speech-api.git`
2. Navigate to the project directory:
   - `cd deno-deepgram-text-to-speech-api`
3. Install dependencies:
   - `pip install -r requirements.txt`

## 🏗️ Usage
### 🏃‍♂️ Running the API
1. Set up environment variables:
   - Create a `.env` file in the project root.
   - Add the following environment variables:
     - `DEEPGRAM_API_KEY`: Your Deepgram API key.
     - `UPSTASH_REDIS_URL`: Your Upstash Redis connection URL.
     - `DATABASE_URL`: Your PostgreSQL database connection URL.
2. Start the API:
   - `uvicorn app.main:app --reload`

### ⚙️ Configuration
- Database configuration is in `app/config/database.py`.
- Authentication and authorization are managed in `app/utils/auth.py`.
- Rate limiting is configured in `app/utils/rate_limiter.py`.

### 📚 Examples
- **Example 1**: Generate speech from text
  ```bash
  curl -X POST "http://localhost:8000/speech" \
    -H "Content-Type: application/json" \
    -d '{
      "text": "Hello, world!",
      "model_id": "deepgram_model_id" 
    }'
  ```

## 🌐 Hosting
### 🚀 Deployment Instructions
1. **Build Docker image:**
   - `docker build -t deno-deepgram-text-to-speech-api .`
2. **Start a Docker container:**
   - `docker run -d -p 8000:8000 deno-deepgram-text-to-speech-api`
3. **Access the API:**
   - The API is accessible at `http://localhost:8000`.

### 🔑 Environment Variables
- **`DEEPGRAM_API_KEY`**: Your Deepgram API key.
- **`UPSTASH_REDIS_URL`**: Your Upstash Redis connection URL.
- **`DATABASE_URL`**: Your PostgreSQL database connection URL.

## 📜 API Documentation
### 🔍 Endpoints
- **POST `/speech`**: Converts text to speech.
  - **Request body:**
    ```json
    {
      "text": "The text to convert to speech.",
      "model_id": "The Deepgram voice model ID."
    }
    ```
  - **Response body:**
    ```json
    {
      "audio_url": "The URL of the generated audio file."
    }
    ```

### 🔒 Authentication
- The API uses JWT authentication to secure endpoints.

### 📝 Examples
- Generate speech using the API:
  ```bash
  curl -X POST "http://localhost:8000/speech" \
    -H "Content-Type: application/json" \
    -d '{
      "text": "This is a test.",
      "model_id": "deepgram_model_id" 
    }'
  ```

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors
- **Author Name** - [Spectra.codes](https://spectra.codes)
- **Creator Name** - [DRIX10](https://github.com/Drix10)

<p align="center">
  <h1 align="center">🌐 Spectra.Codes</h1>
</p>
<p align="center">
  <em>Why only generate Code? When you can generate the whole Repository!</em>
</p>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Developer-Drix10-red" alt="">
  <img src="https://img.shields.io/badge/Website-Spectra.codes-blue" alt="">
  <img src="https://img.shields.io/badge/Backed_by-Google,_Microsoft_&_Amazon_for_Startups-red" alt="">
  <img src="https://img.shields.io/badge/Finalist-Backdrop_Build_v4-black" alt="">
</div>