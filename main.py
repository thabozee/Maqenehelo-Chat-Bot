from src.view.app import build

if __name__ == "__main__":
    app = build()
    app.run(host="0.0.0.0",port="8080",debug=True, use_reloader=True)
