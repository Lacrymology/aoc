def parse(text, fn):
    return [fn(ln.strip()) for ln in text if ln.strip()]
