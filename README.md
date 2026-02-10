# Bajaj Finserv

This project implements two REST APIs as part of the **Chitkara University Qualifier Assignment**.  
The APIs follow a strict response structure, proper status codes, and input validation.

## Objective

Develop and deploy two REST endpoints:

- `POST /bfhl` – performs operations based on input keys
- `GET /health` – returns service health status

## Tech Stack

- Python
- Flask
- REST API architecture
- Deployed on Render

## Live API

Base URL:
https://bajaj-finserv-2-ceix.onrender.com

## API Endpoints

### 1. Health Check

**GET** `/health`

#### Response
json
{
  "is_success": true,
  "official_email": "manya3872.beai23@chitkara.edu.in"
}

