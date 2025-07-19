# GPT Chatbot Web Application

A production-ready, custom GPT chatbot interface with a React frontend and Python FastAPI backend.

- **Frontend:** React, hosted on GitHub Pages
- **Backend:** FastAPI, deployed on Render/Heroku/Railway
- **API:** Secure OpenAI GPT integration

## Structure
- `backend/` — FastAPI backend (Python)
- `frontend/` — React frontend (static)

## Quick Start
See detailed instructions in each subfolder and below.

---

## Step-by-Step Instructions

### 1. Repository Setup
- Clone this repository: `git clone <your-repo-url>`
- Navigate to the project root: `cd gpt-chatbot-app`

### 2. Backend (FastAPI) Setup
- Go to backend folder: `cd backend`
- Copy `.env.example` to `.env` and add your OpenAI API key.
- (Recommended) Create a Python virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Run the API locally:
  ```bash
  uvicorn main:app --reload --port 8000
  ```
- Test at [http://localhost:8000](http://localhost:8000)

#### Deployment (Render/Heroku/Railway)
- Deploy the `backend/` folder as a Python web service.
- Set the environment variable `OPENAI_API_KEY` in your cloud provider.
- Expose port `8000`.
- Example Render build command: `pip install -r requirements.txt`
- Example Render start command: `uvicorn main:app --host 0.0.0.0 --port 8000`

### 3. Frontend (React) Setup
- Go to frontend folder: `cd ../frontend`
- Set the backend API URL in `.env`:
  ```env
  REACT_APP_API_URL=https://<your-backend-deployment-url>/chat
  ```
- Start the React app locally:
  ```bash
  npm install
  npm start
  ```
- Visit [http://localhost:3000](http://localhost:3000)

#### Deployment (GitHub Pages)
- In `frontend/package.json`, set:
  ```json
  "homepage": "https://<your-github-username>.github.io/<repo-name>"
  ```
- Install GitHub Pages deploy tool:
  ```bash
  npm install --save gh-pages
  ```
- Add these scripts to `package.json`:
  ```json
  "predeploy": "npm run build",
  "deploy": "gh-pages -d build"
  ```
- Deploy:
  ```bash
  npm run deploy
  ```

### 4. Security Considerations
- **Never expose your OpenAI API key in frontend code or public repos.**
- Only the backend should have access to the API key.
- Enable CORS in FastAPI to allow requests from your GitHub Pages domain.
- Always use HTTPS in production.

---

## Directory Structure
- `backend/` — FastAPI backend (Python)
- `frontend/` — React frontend (static)

## Credits
- UI: React
- Backend: FastAPI
- Powered by OpenAI GPT
