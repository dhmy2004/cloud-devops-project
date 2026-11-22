from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Cloud DevOps Project</title>
            <meta charset="utf-8">
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 80px; background-color: #f4f6f9; }
                .card { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); display: inline-block; }
                h1 { color: #2c3e50; }
                p { color: #16a085; font-size: 20px; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>أهلاً وسهلاً بكم في مشروعنا السحابي! 🚀</h1>
                <p>Welcome to Abdulrahman &amp; Fares Cloud DevOps Project (Updated v2)</p>
            </div>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
