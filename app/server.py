#!/usr/bin/env python3
from __future__ import annotations

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse
import os


def main() -> int:
    parser = argparse.ArgumentParser(description="Run local demo app server")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()

    web_root = Path(__file__).resolve().parent
    os.chdir(web_root)
    handler = SimpleHTTPRequestHandler
    server = ThreadingHTTPServer((args.host, args.port), handler)
    print(f"[OK] Serving demo app on http://{args.host}:{args.port}")
    print("[INFO] Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[OK] Server stopped.")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
