# BFHL API – Chitkara Qualifier 1 (Class of 2027)

This project implements two REST APIs as part of the Chitkara University Qualifier assessment.  
The APIs follow strict response structures, input validation, and proper HTTP status codes.



## Live API

Base URL:

https://bajaj-finserv-2-ceix.onrender.com

### Endpoints

- `GET /health`
- `POST /bfhl`


## Tech Stack

- Python
- Flask
- REST APIs
- Render (deployment)


## API Details

### 1. Health Check

**Endpoint**

GET /health

**Response**

json
{
  "is_success": true,
  "official_email": "manya3872.beai23@chitkara.edu.in"
}
2. Main API

Endpoint

POST /bfhl


Each request must contain exactly one of the following keys:

Key	Input	Output
fibonacci	Integer	Fibonacci series
prime	Integer array	Prime numbers from array
lcm	Integer array	LCM of numbers
hcf	Integer array	HCF of numbers
AI	Question string	One-word AI response
Request and Response Examples
Fibonacci

Request

{
  "fibonacci": 7
}


Response

{
  "is_success": true,
  "official_email": "manya3872.beai23@chitkara.edu.in",
  "data": [0,1,1,2,3,5,8]
}

Prime

Request

{
  "prime": [2,4,7,9,11]
}


Response

{
  "is_success": true,
  "official_email": "manya3872.beai23@chitkara.edu.in",
  "data": [2,7,11]
}

LCM

Request

{
  "lcm": [12,18,24]
}


Response

{
  "is_success": true,
  "official_email": "manya3872.beai23@chitkara.edu.in",
  "data": 72
}

HCF

Request

{
  "hcf": [24,36,60]
}


Response

{
  "is_success": true,
  "official_email": "manya3872.beai23@chitkara.edu.in",
  "data": 12
}

AI Response

Request

{
  "AI": "What is the capital of Maharashtra?"
}


Response

{
  "is_success": true,
  "official_email": "manya3872.beai23@chitkara.edu.in",
  "data": "Mumbai"
}

Response Format
Success
{
  "is_success": true,
  "official_email": "your_email",
  "data": <result>
}

Error
{
  "is_success": false
}

