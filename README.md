# DNA Detection Project

## Public API
**URL**: https://mutantdetection.onrender.com/docs

**Considerations**: This API is running in a free hosting service, so it may delay the first request. That is because the server is down for inactivity and needs to run from 0 again.

## Installation of dependencies requried

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To use the mutant detector, follow these steps:

1. Clone the repository:
  ```bash
  git clone https://github.com/yourusername/dnaDetection.git
  ```
2. Navigate to the project directory:
  ```bash
  cd dnaDetection
  ```
3. Run the following command to open a local server:
  ```bash
  uvicorn main:app --reload --port 8001
  ```
4. Open a new tab y your browser:
  ```bash
    http://127.0.0.1:8001/docs
  ```
5. Explore the endpoints

6. The '/' endpoints gives you 2 DNA examples for you to try!!

## Development
This project was developed by **Santiago Herrera**, using **Python** and **FastAPI**