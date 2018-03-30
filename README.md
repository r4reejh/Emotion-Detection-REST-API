# REST-emo-detect
REST Emotion Detection API

## Additional modules required (Linux)
```python
pip install falcon
pip install gunicorn
```
## How to run (Linux)
```python
gunicorn server:app
```
## Modules Required and how to run (Windows)
```python
pip install falcon
pip install waitress
waitress-serve --port=8000 server:app
```

## Head over to
<http://localhost:8000>
