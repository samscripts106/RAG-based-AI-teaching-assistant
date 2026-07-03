import os
import json

folder = "jsons"

print("\n🔍 Scanning JSON files...\n")

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    if not file.endswith(".json"):
        print(f"⏭️ Skipping non-json file: {file}")
        continue

    try:
        # Step 1: Try reading raw bytes first (detect corruption)
        with open(path, "rb") as f:
            raw = f.read()

        # Quick sanity check
        if b"\x00" in raw:
            print(f"❌ BINARY FILE DETECTED: {file}")
            continue

        # Step 2: Try decoding as UTF-8
        text = raw.decode("utf-8")

        # Step 3: Try parsing JSON
        data = json.loads(text)

        # Step 4: Validate expected structure
        if "chunks" not in data:
            print(f"⚠️ INVALID STRUCTURE (missing 'chunks'): {file}")
        else:
            print(f"✅ OK: {file} | chunks = {len(data['chunks'])}")

    except UnicodeDecodeError as e:
        print(f"❌ UTF-8 ERROR in {file}")
        print(f"   → {e}")

    except json.JSONDecodeError as e:
        print(f"❌ JSON FORMAT ERROR in {file}")
        print(f"   → {e}")

    except Exception as e:
        print(f"❌ UNKNOWN ERROR in {file}")
        print(f"   → {e}")

print("\n🏁 Done checking files.\n")