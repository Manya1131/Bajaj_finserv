from flask import Flask, request, jsonify
import os
import google.generativeai as genai
app = Flask(__name__)

EMAIL = "manya3872.beai23@chitkara.edu.in"

GEMINI_API_KEY = "AIzaSyCSwSZoGX1nBCAfNr55BUOAkHPhvAjR0y4"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

print("API KEY:", GEMINI_API_KEY)
def fibonacci(n):
    arr = [0, 1]
    for i in range(2, n):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr[:n]


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_primes(arr):
    return [x for x in arr if is_prime(x)]


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def hcf(arr):
    res = arr[0]
    for num in arr[1:]:
        res = gcd(res, num)
    return res


def lcm(arr):
    def lcm2(a, b):
        return (a * b) // gcd(a, b)

    res = arr[0]
    for num in arr[1:]:
        res = lcm2(res, num)
    return res

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "is_success": True,
        "official_email": EMAIL
    })


@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        body = request.get_json()
        if not body:
            return jsonify({"is_success": False}), 400

        if "fibonacci" in body:
            n = body["fibonacci"]
            if not isinstance(n, int) or n < 0:
                return jsonify({"is_success": False}), 400

            return jsonify({
                "is_success": True,
                "official_email": EMAIL,
                "data": fibonacci(n)
            })

        if "prime" in body:
            arr = body["prime"]
            if not isinstance(arr, list):
                return jsonify({"is_success": False}), 400

            return jsonify({
                "is_success": True,
                "official_email": EMAIL,
                "data": get_primes(arr)
            })

        if "hcf" in body:
            return jsonify({
                "is_success": True,
                "official_email": EMAIL,
                "data": hcf(body["hcf"])
            })

        if "lcm" in body:
            return jsonify({
                "is_success": True,
                "official_email": EMAIL,
                "data": lcm(body["lcm"])
            })

        if "AI" in body:
            question = body["AI"]

            try:
                response = model.generate_content(
                    f"Answer in one word only: {question}"
                )
                print("RAW RESPONSE:", response)
                answer = response.text
            except Exception as e:
                print("AI ERROR:", e)
                answer = "Error"

            return jsonify({
                "is_success": True,
                "official_email": EMAIL,
                "data": answer
            })



        return jsonify({"is_success": False}), 400

    except Exception:
        return jsonify({"is_success": False}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
