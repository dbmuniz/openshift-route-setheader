from flask import Flask
import os

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route('/')
def hello():

    print("\n--- Headers HTTP ---")
    for key, value in request.headers.items():
        print(f"{key}: {value}")
    print("-----------------------------------")
    
    return "Hello World!"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
