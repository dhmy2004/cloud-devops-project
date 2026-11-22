from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Cloud DevOps Project</title>
            <meta charset="utf-8">
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h1>Cloud DevOps Project</h1>
            <p>Application deployed successfully! - Updated by Abdulrahman &amp; Fares (v2)</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
